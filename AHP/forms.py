from django.forms import ModelForm
from django import forms
from AHP.models import *


class form_hp(ModelForm):
    class Meta:
        model = handphone
        fields = '__all__'

        widgets = {
            'merk': forms.TextInput({'class': 'form-control'}),
            'design': forms.Select({'class': 'form-control'}),
            'storage': forms.NumberInput({'class': 'form-control'}),
            'harga': forms.NumberInput({'class': 'form-control'}),
            'peforma': forms.Select({'class': 'form-control'}),
        }


class form_penting(ModelForm):
    class Meta:
        model = kepentingan
        fields = '__all__'
