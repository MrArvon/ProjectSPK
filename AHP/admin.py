from django.contrib import admin
from AHP.models import *


class setAdmin(admin.ModelAdmin):
    list_display = ['merk', 'design', 'storage', 'harga', 'peforma']
    search_fields = ['merk', 'design', 'storage', 'harga', 'peforma']
    list_filter = ('design', 'peforma')
    list_per_page = 10


# class setAdmin2(admin.ModelAdmin):
#     list_display = ['kategori', 'nilai_penting']
#     list_per_page = 10


admin.site.register(handphone, setAdmin)
admin.site.register(design)
admin.site.register(peforma)
admin.site.register(kepentingan)
# admin.site.register(nilai_penting)
