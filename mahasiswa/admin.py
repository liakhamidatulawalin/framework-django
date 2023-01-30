from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis, Jenis_prabot, perabotan, aksesoris


class KolomBarang(admin.ModelAdmin):
    list_display = ['kode', 'nama', 'stok', 'link_gbr', 'jenis_id']
    search_fields = ['kode', 'nama']
    list_filter = ('jenis_id',)
    list_per_page = 3


class KolomPerabotan(admin.ModelAdmin):
    list_display = ['kode', 'nama', 'jenis', 'harga']
    search_fields = ['kode', 'nama']
    list_filter = ('jenis',)
    list_per_page = 5


class KolomAksesoris(admin.ModelAdmin):
    list_display = ['kode', 'nama', 'stok', 'harga']
    search_fields = ['kode', 'nama']
    list_per_page = 5


admin.site.register(Barang, KolomBarang)
admin.site.register(Jenis)
admin.site.register(perabotan, KolomPerabotan)
admin.site.register(aksesoris, KolomAksesoris)
admin.site.register(Jenis_prabot)
