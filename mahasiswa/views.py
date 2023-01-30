from django.shortcuts import render, redirect
from mahasiswa.forms import form_barang, form_perabotan, form_aksesoris
from mahasiswa.models import Barang, perabotan, aksesoris
from django.contrib import messages
# Create your views here.


def home(request):
    nama = "Home"
    konteks = {
        'title': nama,
    }
    return render(request, 'home.html', konteks)


def tambah_barang(request):
    if request.POST:
        form = form_barang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil disimpan')
            form = form_barang()
            konteks = {
                'form': form,
            }
            return render(request, 'tambah_barang.html', konteks)
    else:
        form = form_barang
        konteks = {
            'form': form,
        }
    return render(request, 'tambah_barang.html', konteks)


def update_brg(request, id_barang):
    barangs = Barang.objects.get(id=id_barang)
    if request.POST:
        form = form_barang(request.POST, instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil diubah')
            return redirect('update_brg', id_barang=id_barang)
    else:
        form = form_barang(instance=barangs)
        konteks = {
            'form': form,
            'barangs': barangs,
        }
    return render(request, 'update_brg.html', konteks)


def delete_brg(request, id_barang):
    barangs = Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request, 'Data berhasil dihapus')
    return redirect('barang')


def Barang_view(request):
    barangs = Barang.objects.all()
    konteks = {
        'barangs': barangs
    }
    return render(request, 'tampil_barang.html', konteks)

# todo ==> tabel baru


def tambah_perabotan(request):
    if request.POST:
        form = form_perabotan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil disimpan')
            form = form_perabotan()
            konteks = {
                'form': form,
            }
            return render(request, 'tambah_perabotan.html', konteks)
    else:
        form = form_perabotan()
        konteks = {
            'form': form,
        }
    return render(request, 'tambah_perabotan.html', konteks)


def update_prabot(request, id_prabot):
    perabotans = perabotan.objects.get(id=id_prabot)
    if request.POST:
        form = form_perabotan(request.POST, instance=perabotans)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil di ubah")
            return redirect('ubahPra', id_prabot=id_prabot)
    else:
        form = form_perabotan(instance=perabotans)
        konteks = {
            'form': form,
            'perabotans': perabotans,
        }
    return render(request, 'update_prabot.html', konteks)


def delete_prabot(request, id_prabot):
    perabotans = perabotan.objects.filter(id=id_prabot)
    perabotans.delete()
    messages.success(request, 'Data berhasil dihapus')
    return redirect('perabotan')


def tampil_perabotan(request):
    Perabotans = perabotan.objects.all()
    konteks = {
        'Perabotans': Perabotans,
    }
    return render(request, 'tampil_perabotan.html', konteks)


def tambah_aksesoris(request):
    if request.POST:
        form = form_aksesoris(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil ditambahkan')
            form = form_aksesoris()
            konteks = {
                'form': form,
            }
            return render(request, 'tambah_aksesoris.html', konteks)
    else:
        form = form_aksesoris()
        konteks = {
            'form': form,
        }
        return render(request, 'tambah_aksesoris.html', konteks)


def update_akses(request, id_akses):
    aksesoriss = aksesoris.objects.get(id=id_akses)
    if request.POST:
        form = form_aksesoris(request.POST, instance=aksesoriss)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil di update")
            return redirect('ubahAkses', id_akses=id_akses)
    else:
        form = form_aksesoris(instance=aksesoriss)
        konteks = {
            'form': form,
            'aksesoriss': aksesoriss,
        }
    return render(request, 'update_akses.html', konteks)


def delete_akses(request, id_akses):
    aksesoriss = aksesoris.objects.filter(id=id_akses)
    aksesoriss.delete()
    messages.success(request, 'Data berhasil dihapus')
    return redirect('aksesoris')


def tampil_aksesoris(request):
    Aksesoriss = aksesoris.objects.all()
    konteks = {
        'Aksesoriss': Aksesoriss,
    }
    return render(request, 'tampil_aksesoris.html', konteks)
