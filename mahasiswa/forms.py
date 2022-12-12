from django import forms
from django.forms import ModelForm
from mahasiswa.models import Barang


class form_barang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'

        widgets = {
            # nama pada widget harus sana dengan pada file models.py
            'Kode': forms.TextInput({'class': 'form-control'}),
            'Nama': forms.TextInput({'class': 'form-control'}),
            'Stok': forms.NumberInput({'class': 'form-control'}),
            'Harga': forms.NumberInput({'class': 'form-control'}),
            'Link gbr': forms.Select({'class': 'form-control'}),
        }
