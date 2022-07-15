from django.shortcuts import render, redirect
from AHP.models import *
from AHP.forms import form_hp, form_penting
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import numpy as np
# from django.http import HttpResponse


@login_required(login_url=settings.LOGIN_URL)
def pendataan(request):
    phone = handphone.objects.all()
    desain = design.objects.all()
    peform = peforma.objects.all()
    penting = kepentingan.objects.get(id=1)
    penting2 = [penting.design, penting.storage, penting.harga, penting.peforma]
    judul = ['Design', 'Storage', 'Harga', 'Peforma']
    konteks = {
        'isi': phone,
        'isi_design': desain,
        'isi_peforma': peform,
        'isi_penting': zip(judul, penting2),
    }
    return render(request, "menu_data.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def pengeditan(request, id_handphone):
    Handphone = handphone.objects.get(id=id_handphone)
    template = 'menu_edit.html'
    if request.POST:
        form = form_hp(request.POST, instance=Handphone)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Telah Diubah")
            return redirect('pengeditan', id_handphone=id_handphone)
    else:
        form = form_hp(instance=Handphone)
        konteks = {
            'form': form,
            'isi': Handphone
        }
        return render(request, template, konteks)


def premis(a):
    tampung = [1 / 7, 1 / 5, 1 / 3, 1, 3, 5, 7]
    pos = 3
    temp = []
    total = []
    for i in range(len(a)):
        temp2 = []
        tot = 0
        for j in range(len(a)):
            temp2.append(round(tampung[int(pos + ((a[i] - a[j]) / 2))], 3))
            tot += tampung[int(pos + (-1 * (a[i] - a[j]) / 2))]
        temp.append(temp2)
        total.append(round(tot, 3))
    temp.append(total)
    return temp


def normalisasi(a):
    temp = []
    for i in range(len(a) - 1):
        temp2 = []
        tot = 0
        for j in range(len(a) - 1):
            temp2.append(round(a[i][j] / a[4][j], 3))
            tot += a[i][j] / a[4][j]

        temp2.append(round((tot / (len(a) - 1)), 3))
        temp.append(temp2)

    temp.append([round(sum(x), 2) for x in zip(*temp)])
    return temp


def pairwise_kali_Wkriteria(a, b):
    #print(len(a))
    wKriteria = []
    pairwise = []
    #pairwise tanpa total bawah
    for i in range(len(a)-1):
      tamp = []
      for j in range(len(a)-1):
        tamp.append(a[i][j])
      pairwise.append(tamp)
    #print(pairwise)
    # wkriteria
    for i in range(len(b)-1):
      tamp = []
      tamp.append(b[i][4])
      wKriteria.append(tamp)
    #print(wKriteria)
    return pairwise, wKriteria, perkalian_matrix(pairwise, wKriteria)


def perkalian_matrix(a, b):
    temp = np.matmul(a, b)
    temp = np.around(temp, decimals=3)
    return temp


def wKriteria_bagi_pairwiseKaliwKriteria(a, b):
    temp = []
    temp3 = []
    temp2 = []
    temp4 = []
    for i in range(len(a)):
        temp3.append(a[i][0])
        temp4.append(b[i][0])
        temp2.append(round(a[i][0] / b[i][0], 3))
    temp.append(temp3)
    temp.append(temp4)
    temp.append(temp2)
    return temp


def total_wKriteria_bagi_pairwiseKaliwKriteria(a):
    return (np.sum(a[2]))


def hitung_t(a, n):
    return round((a/n), 3)


def hitung_CI(t, n):
    return round((t-n)/(n-1), 3)


def hitung_CR(a,n):
    RIn = {
        2: 0,
        3: 0.58,
        4: 0.9,
        5: 1.12,
        6: 1.24,
        7: 1.32
    }
    return round(a/RIn[n], 3)


def apakah_Konsisten(CR):
    if CR < 0.1:
        return "Konsisten"
    else:
        return "Tidak Konsisten"


def normalisasi_alternatif_desain(alternatif):
    a = np.array(alternatif)
    desain = []
    hasil_d = []
    total = a[:, 0].sum()
    tot_normal = 0
    for i in range (len(alternatif)):
        desain.append(alternatif[i][0])
        hasil_d.append(round(alternatif[i][0]/total, 3))
        tot_normal += hasil_d[i]
    desain.append(total)
    hasil_d.append(round(tot_normal, 2))
    return desain, hasil_d


def normalisasi_alternatif_storage(alternatif):
    a = np.array(alternatif)
    storage = []
    hasil_s = []
    total = a[:,1].sum()
    tot_normal = 0
    for i in range (len(alternatif)):
        storage.append(alternatif[i][1])
        hasil_s.append(round(alternatif[i][1]/total, 3))
        tot_normal += hasil_s[i]
    storage.append(total)
    hasil_s.append(round(tot_normal, 2))
    return storage, hasil_s


def normalisasi_alternatif_harga(alternatif):
    a = np.array(alternatif)
    harga = []
    hasil_h = []
    min = a[:, 2].min()
    tot_normal = 0
    harga_bobot_altenatif = []
    for i in range(len(alternatif)):
        harga_bobot_altenatif.append(round(min/alternatif[i][2], 3))
        harga.append(alternatif[i][2])
    hba = np.array(harga_bobot_altenatif)
    total = hba.sum()
    for i in range(len(harga)):
        hasil_h.append(round(harga_bobot_altenatif[i]/total, 3))
        tot_normal += hasil_h[i]
    harga_bobot_altenatif.append(round(total, 3))
    harga.append(a[:, 2].sum())
    hasil_h.append(round(tot_normal, 2))
    return harga, harga_bobot_altenatif, hasil_h


def normalisasi_alternatif_performa(alternatif):
    a = np.array(alternatif)
    performa = []
    hasil_p = []
    total = a[:, 3].sum()
    tot_normal = 0
    for i in range (len(alternatif)):
        performa.append(alternatif[i][3])
        hasil_p.append(round(alternatif[i][3]/total, 3))
        tot_normal += hasil_p[i]
    performa.append(total)
    hasil_p.append(round(tot_normal, 2))
    return performa, hasil_p


def W_Alternatif_perKriteria(na_d, na_s, na_h, na_p):
    temp = []
    for i in range(len(na_d)):
        temp.append([na_d[i], na_s[i], na_h[i], na_p[i]])
    return temp


def wap_kali_Wkriteria(wap, WK):
    # tampungan sementara menyimpan isi tabel wap tanpa total pada baris ke 4
    temp1 = []
    temp2 = []
    temp3 = []
    for i in range(len(wap)-1):
        temp1.append(wap[i])
    temp2 = perkalian_matrix(temp1, WK)
    for i in range(len(temp2)):
        temp3.append(temp2[i][0])
    # operasi perkalian matriks
    return temp1, temp3


def rank(nama_alternatif, hasil_akhir):
    temp = []
    for i in range(len(nama_alternatif)):
        temp.append([nama_alternatif[i], hasil_akhir[i]])
    temp.sort(reverse= True,key = lambda temp: temp[1])
    return temp


@login_required(login_url=settings.LOGIN_URL)
def perhitungan(request):
    phone = handphone.objects.all()
    mer = handphone.objects.values_list('merk')
    merk = []
    merk1 = []
    for i in range(len(mer)):
        merk.append(mer[i][0])
        merk1.append(mer[i][0])
    merk.append('Total')
    lmerk = (len(merk))
    des = handphone.objects.values_list('design__nilai').order_by('id')
    sto = handphone.objects.values_list('storage')
    har = handphone.objects.values_list('harga')
    pef = handphone.objects.values_list('peforma__nilai').order_by('id')
    penting = kepentingan.objects.get(id=1)
    penting2 = [penting.design, penting.storage, penting.harga, penting.peforma]
    penampungan = []
    for i in range(len(des)):
        penampungan.append([des[i][0], sto[i][0], har[i][0], pef[i][0]])
    hasil = premis(penting2)
    hasil2 = normalisasi(premis(penting2))
    pairwise, wKriteria, hasil3 = pairwise_kali_Wkriteria(hasil, hasil2)
    wbagiaw = wKriteria_bagi_pairwiseKaliwKriteria(hasil3, wKriteria)
    Tot_wbagiaw = total_wKriteria_bagi_pairwiseKaliwKriteria(wbagiaw)
    t = hitung_t(Tot_wbagiaw, len(penting2))
    CI = hitung_CI(t, len(penting2))
    IRn = [[2, 0], [3, 0.58], [4, 0.9], [5, 1.12], [6, 1.24], [7, 1.32]]
    CR = hitung_CR(CI, len(penting2))
    konsisten = apakah_Konsisten(CR)
    d, na_d = normalisasi_alternatif_desain(penampungan)
    s, na_s = normalisasi_alternatif_storage(penampungan)
    h, hba, na_h = normalisasi_alternatif_harga(penampungan)
    p, na_p = normalisasi_alternatif_performa(penampungan)
    wap = W_Alternatif_perKriteria(na_d, na_s, na_h, na_p)
    wap_tanpa_total, hasil_akhir = wap_kali_Wkriteria(wap, wKriteria)
    hasil_rank = rank(merk1, hasil_akhir)
    konteks = {
        'isi': phone,
        'isi_penting': penting2,
        'matriks_utama': penampungan,
        'premis': hasil,
        'normalisasi': hasil2,
        'pairwise': pairwise,
        'wKriteria': wKriteria,
        'hasil3': hasil3,
        'wbagiaw': wbagiaw,
        'Tot_wbagiaw': Tot_wbagiaw,
        't': t,
        'CI': CI,
        'IRn': IRn,
        'CR': CR,
        'konsisten': konsisten,
        'lmerk': lmerk,
        'd': zip(merk, d),
        'na_d': zip(merk, na_d),
        's': zip(merk, s),
        'na_s': zip(merk, na_s),
        'h': zip(merk, h, hba),
        'na_h': zip(merk, na_h),
        'p': zip(merk, p),
        'na_p': zip(merk, na_p),
        'wap': wap,
        'wap_tanpa_total': wap_tanpa_total,
        'hasil_akhir': hasil_akhir,
        'rank': hasil_rank,
    }
    return render(request, "menu_hitung.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_hp(request):
    if request.POST:
        form = form_hp(request.POST)
        if form.is_valid():
            form.save()
            form = form_hp()
            pesan = "Data Tersimpan"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah_data.html', konteks)

    else:
        form = form_hp()
        konteks = {
            'form': form,
        }
        return render(request, "tambah_data.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus_data(request, id_handphone):
    phone = handphone.objects.filter(id=id_handphone)
    phone.delete()
    messages.success(request, "Data Telah Dihapus!")
    return redirect('pendataan')


@login_required(login_url=settings.LOGIN_URL)
# def edit_penting(request):
#     # return HttpResponse(escape(repr(request)))
#     penting = kepentingan.objects.all()
#     template = 'edit_penting.html'
#     penting2 = nilai_penting.objects.all()
#     if request.POST:
#         form = form_penting(request.POST, instance=penting.first())
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Data Telah Diubah")
#             return redirect('pendataan')
#     else:
#         form = form_penting(instance=penting.first())
#         konteks = {
#             'form': form,
#             'penting': penting,
#             'penting2': penting2,
#             'request': request,
#         }
#         return render(request, template, konteks)


def edit_penting(request):
    penting = kepentingan.objects.get(id=1)
    penting2 = [penting.design, penting.storage, penting.harga, penting.peforma]
    if request.POST:
        form = form_penting(request.POST, instance=penting)
        if form.is_valid():
            form.save()
            return redirect('pendataan')
    else:
        penting = kepentingan.objects.get(id=1)
        form = form_penting(request.POST, instance=penting)

        konteks = {
            'form': form,
            'isi0': penting,
            'isian': penting2,
            'isi1': penting2[0],
            'isi2': penting2[1],
            'isi3': penting2[2],
            'isi4': penting2[3],
        }
        return render(request, 'edit_penting.html', konteks)


# def edit_penting2(request):
#     return HttpResponse(request.POST.items())
