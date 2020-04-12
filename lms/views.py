from django.shortcuts import render
from django.views.generic.list import ListView


from .models import Patron


def home(request):
    context = {'page': 'home'}
    return render(request, 'home.html', context)


class ListPatronsView(ListView):
    context_object_name = 'patrons'
    model = Patron
    template_name = 'patrons.html'

    def get_context_data(self, **kwargs):
        # call the base implementation fist to get a context
        context = super().get_context_data(**kwargs)
        # add page variable
        context['page'] = 'patrons'
        return context
