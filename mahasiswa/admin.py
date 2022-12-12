from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis


class KolomBarang(admin.ModelAdmin):
    list_display = ['kode', 'nama', 'stok', 'link_gbr', 'jenis_id']
    search_fields = ['kode', 'nama']
    list_filter = ('jenis_id',)
    list_per_page = 3


admin.site.register(Barang, KolomBarang)
admin.site.register(Jenis)
