"""asia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from dashboard.views import produk
from mahasiswa.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('produk/', produk, name='produk'),
    path('barang/', tambah_barang, name='add_barang'),
    path('ubahbrg/<int:id_barang>', update_brg, name='update_brg'),
    path('hapusbrg/<int:id_barang>', delete_brg, name='hapus_brg'),
    path('brgView/', Barang_view, name='barang'),
    path('addPrabot/', tambah_perabotan, name='add_prabot'),
    path('ubahPra/<int:id_prabot>', update_prabot, name='ubahPra'),
    path('deletePra/<int:id_prabot>', delete_prabot, name='hapus_prabot'),
    path('perabotan/', tampil_perabotan, name='perabotan'),
    path('addAkses/', tambah_aksesoris, name='addAkses'),
    path('ubahAkses/<int:id_akses>', update_akses, name='ubahAkses'),
    path('deleteAkses/<int:id_akses>', delete_akses, name='hapus_akses'),
    path('aksesoris/', tampil_aksesoris, name='aksesoris'),
]
