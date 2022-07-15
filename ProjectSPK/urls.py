from django.contrib import admin
from django.urls import path
from AHP.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/masuk/', permanent=True)),
    path('admin/', admin.site.urls),
    path('menu_data/', pendataan, name='pendataan'),
    path('menu_data/menu_edit/<int:id_handphone>', pengeditan, name='pengeditan'),
    path('menu_hitung/', perhitungan, name='perhitungan'),
    path('tambah_data/', tambah_hp, name='penambahan'),
    path('menu_data/hapus/<int:id_handphone>', hapus_data, name='penghapusan'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('edit_penting/', edit_penting, name='edit_penting'),
    # path('a', edit_penting2, name='a')
]
