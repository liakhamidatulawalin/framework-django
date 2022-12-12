from django.shortcuts import render

# Create your views here.


def produk(request):
    nama = 'Produk'
    konteks = {
        'title': nama,
    }
    return render(request, 'produk.html', konteks)
