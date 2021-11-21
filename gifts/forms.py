from django import forms
from django.forms import fields

from .models import Gifts

class GiftConformation(forms.ModelForm):
    class Meta: 
        model=Gifts
        fields = ['taken']