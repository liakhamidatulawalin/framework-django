from django.db import models

# Create your models here.

class Jenis(models.Model):
    nama = models.CharField(max_length=50)
    ket = models.TextField()

    def __str__(self):
        return self.nama


class Barang(models.Model):
    kode = models.CharField(max_length=8)
    nama = models.CharField(max_length=100)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gbr = models.CharField(max_length=200, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama

# todo : Tabel baru


class Jenis_prabot(models.Model):
    kode = models.CharField(max_length=8)
    nama = models.CharField(max_length=30)
    ket = models.CharField(max_length=80)

    def __str__(self):
        return self.nama


class perabotan(models.Model):
    kode = models.CharField(max_length=8)
    nama = models.CharField(max_length=30)
    harga = models.BigIntegerField()
    jenis = models.ForeignKey(
        Jenis_prabot, on_delete=models.CASCADE, null=True)
    deskrip = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class aksesoris(models.Model):
    kode = models.CharField(max_length=8)
    nama = models.CharField(max_length=30)
    stok = models.IntegerField()
    harga = models.BigIntegerField()

    def __str__(self):
        return self.nama
