from django.shortcuts import render
from mahasiswa.forms import form_barang
from mahasiswa.models import Barang
# Create your views here.


def tambah_barang(request):
    form = form_barang
    konteks = {
        'form': form,
    }
    return render(request, 'tambah_barang.html', konteks)


def Barang_view(request):
    barangs = Barang.objects.all()
    konteks = {
        'barangs': barangs
    }
    return render (request, 'tampil_barang.html', konteks)