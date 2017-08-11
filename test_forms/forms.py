import itertools

# DJANGO import
from django import forms
from django.utils.text import slugify

# LOCAL APP import
from . import models

class Sect1Form(forms.ModelForm):

    class Meta:
        model = models.Sect1
        exclude = [
            'ts1_number',
            'title'
        ]

    

class Sect2Form(forms.ModelForm):

    class Meta:
        model = models.Sect2
        exclude = [
            'ts2_number',
            'title'
        ]

class CompleteTestForm(forms.ModelForm):

    class Meta:
        model = models.CompleteTest
        fields = [
            'address',
        ]

    

    

class Section1Form(forms.Form):
    test = forms.CharField(max_length=255)

class Section2Form(forms.Form):
    test2 = forms.CharField(max_length=255)
