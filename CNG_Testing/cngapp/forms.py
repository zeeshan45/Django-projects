from django import forms
from .models import Cngmodel

class UploadImage(forms.ModelForm):
    class Meta:
        model = Cngmodel
        fields = ['image']

class CngForm(forms.ModelForm):
    class Meta:
        model = Cngmodel
        fields = '__all__'
