from django import forms
from django.forms import ModelForm
from mahasiswa.models import Barang, perabotan, aksesoris


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

# todo ==> form baru


class form_perabotan(ModelForm):
    class Meta:
        model = perabotan
        fields = '__all__'

        widgets = {
            'kode': forms.TextInput({'class': 'form-control'}),
            'nama': forms.TextInput({'class': 'form-control'}),
            'harga': forms.TextInput({'class': 'form-control'}),
            'jenis': forms.Select({'class': 'form-control'}),
            'deskrip': forms.TextInput({'class': 'form-control'})
        }


class form_aksesoris(ModelForm):
    class Meta:
        model = aksesoris
        fields = '__all__'

        widgets = {
            'kode': forms.TextInput({'class': 'form-control'}),
            'nama': forms.TextInput({'class': 'form-control'}),
            'stok': forms.TextInput({'class': 'form-control'}),
            'harga': forms.TextInput({'class': 'form-control'}),
        }
