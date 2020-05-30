from django import forms

from .models import Patron


class PatronForm(forms.ModelForm):
    class Meta:
        model = Patron
        fields = ['first_name', 'last_name', 'address',
                  'date_of_birth', 'telephone', 'gender']
