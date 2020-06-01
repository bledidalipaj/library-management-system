import json


from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    View
)

from .forms import PatronForm
from .models import Book, Checkout, CheckoutHistory, Hold, LibraryCard, Patron
from .utils import STATUS_DICT


def home(request):
    context = {'page': 'home'}
    return render(request, 'home.html', context)


def checkin_item(request):
    if request.is_ajax():
        checkout_ids = map(int, request.GET.get('checkout_ids').split(','))

        for pk in checkout_ids:
            checkout = get_object_or_404(Checkout, pk=pk)
            checkout.delete()

        data = {
            'status': 'Ok'
        }
        return JsonResponse(data)


def get_item_metadata(request, pk):

    if request.is_ajax():
        library_asset = get_object_or_404(Book, pk=pk)
        context = {
            'status': STATUS_DICT[library_asset.status.name],
            'available_copies': library_asset.number_of_available_copies_to_borrow,
        }

        return JsonResponse(context)
    else:
        raise Http404()


def get_checkout_history(request, pk):
    library_asset = get_object_or_404(Book, pk=pk)

    if request.is_ajax():
        checkout_history = CheckoutHistory.objects.filter(
            library_asset=library_asset)[:5]
    else:
        checkout_history = CheckoutHistory.objects.filter(
            library_asset=library_asset)

    context = {
        'checkout_history': checkout_history,
    }

    return render(request, 'partials/_checkout_history.html', context)


def get_holds(request, pk):
    library_asset = get_object_or_404(Book, pk=pk)

    if request.is_ajax():
        holds = Hold.objects.filter(
            library_asset=library_asset)[:5]
    else:
        holds = Hold.objects.filter(
            library_asset=library_asset)

    context = {
        'holds': holds,
    }

    return render(request, 'partials/_holds.html', context)


def get_item_checkouts(request, pk):
    library_asset = get_object_or_404(Book, pk=pk)
    context = {
        'checkouts': Checkout.objects.filter(library_asset=library_asset).order_by('library_card'),
        'pk': pk
    }

    return render(request, 'partials/_modal_content.html', context)


class CheckoutItemView(SuccessMessageMixin, CreateView):
    model = Checkout
    fields = ['library_card']
    template_name = 'checkout.html'
    success_message = 'Item checked successfuly.'

    def form_valid(self, form):
        library_asset = get_object_or_404(Book, pk=self.kwargs['pk'])
        form.instance.library_asset = library_asset
        return super(CheckoutItemView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CheckoutItemView, self).get_context_data(**kwargs)
        context['library_asset_id'] = self.kwargs['pk']
        context['item'] = get_object_or_404(Book, pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('item-detail', kwargs={'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
        except ValidationError as e:
            messages.add_message(request, messages.WARNING, e.message)
            return render(request, template_name=self.template_name, context=self.get_context_data())
        return redirect(self.get_success_url())


class LibraryItemDetailView(DetailView):
    context_object_name = 'item'
    model = Book
    template_name = 'item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LibraryItemDetailView, self).get_context_data(**kwargs)
        library_asset = get_object_or_404(Book, pk=self.kwargs['pk'])
        context['checkout_history'] = CheckoutHistory.objects.filter(
            library_asset=library_asset)[:5]
        context['holds'] = Hold.objects.filter(library_asset=library_asset)

        return context


class ListPatronsView(ListView):
    context_object_name = 'patrons'
    model = Patron
    template_name = 'patrons.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        # call the base implementation fist to get a context
        context = super().get_context_data(**kwargs)
        # add page variable
        context['page'] = 'patrons'
        return context


class ListCatalogView(ListView):
    context_object_name = 'books'
    model = Book
    template_name = 'catalog.html'
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        # call the base implementation fist to get a context
        context = super().get_context_data(**kwargs)
        # add page variable
        context['page'] = 'catalog'
        return context


class PlaceHoldItemView(SuccessMessageMixin, CreateView):
    model = Hold
    fields = ['library_card']
    template_name = 'place_hold.html'
    success_message = 'Hold was successfuly placed.'

    def form_valid(self, form):
        library_asset = get_object_or_404(Book, pk=self.kwargs['pk'])
        form.instance.library_asset = library_asset
        return super(PlaceHoldItemView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PlaceHoldItemView, self).get_context_data(**kwargs)
        context['library_asset_id'] = self.kwargs['pk']
        context['item'] = get_object_or_404(Book, pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('item-detail', kwargs={'pk': self.kwargs['pk']})


class PatronDetailView(SuccessMessageMixin, View):

    def get(self, request, pk):
        patron = get_object_or_404(Patron, pk=pk)
        patron_card = get_object_or_404(LibraryCard, patron=patron)

        context = {
            'patron': patron,
            'checkout_history': CheckoutHistory.objects.filter(library_card=patron_card),
            'checkouts': Checkout.objects.filter(library_card=patron_card)
        }

        return render(request, 'patron_detail.html', context)

    def post(self, request, pk):
        '''
        Check in selected items by removing the checkouts from the database.
        After the successful deletion we redirect to the same view.
        '''
        checkout_ids = request.POST.getlist('item-id')
        items_count = len(checkout_ids)
        success_message = f'Successfully returned {items_count}' + [
            ' items.', ' item.'][items_count == 1]

        for checkout_id in checkout_ids:
            checkout_obj = get_object_or_404(Checkout, pk=checkout_id)
            checkout_obj.delete()

        messages.success(request, success_message)

        return HttpResponseRedirect(self.request.path_info)


class PatronUpdateView(SuccessMessageMixin, UpdateView):
    model = Patron
    fields = '__all__'
    template_name = 'update_patron.html'
    success_message = 'Patron infromation updated successfuly.'

    def get_success_url(self):
        return reverse_lazy('patron', kwargs={'pk': self.kwargs['pk']})
