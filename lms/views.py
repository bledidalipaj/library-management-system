from django.shortcuts import render
from django.views.generic.list import ListView


from .models import Patron


def home(request):
    return render(request, 'home.html')


class ListPatronsView(ListView):
	context_object_name = 'patrons'
	model = Patron
	template_name = 'patrons.html'
