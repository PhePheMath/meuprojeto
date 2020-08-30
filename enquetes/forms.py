from django import forms
from .models import Enquetes

class EnqueteForm(forms.ModelForm):

    class Meta:
        model = Enquetes
        exclude = []


