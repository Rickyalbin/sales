from django.shortcuts import render, redirect
from mobil.models import Merek, Produk

def mobil_list(request):
    template_name = 'mobil_list.html'
    produk_list = Produk.objects.all()
    context = {
        'title':'Halaman Barang',
        'produk':produk_list
    }
    return render(request, template_name, context)

def mobil_add(request):
    template_name = 'mobil_add.html'
    merek = Merek.objects.all()
    if request.method == "POST":

        input_merek = request.POST.get('merek')
        input_nama = request.POST.get('nama')
        input_deskripsi = request.POST.get('deskripsi')
        input_harga = request.POST.get('harga')

        get_merek = Merek.objects.get(nama=input_merek)

        Produk.objects.create(
            nama = input_nama,
            deskripsi = input_deskripsi,
            harga = input_harga,
            merek = get_merek,

        )
        return redirect(mobil_list)
    context = {
        'title':'Halaman Tambah Barang',
        'merek':merek
    }
    return render(request, template_name, context)

def mobil_update(request, id):
    template_name = 'mobil_add.html'
    merek = Merek.objects.all()
    get_produk = Produk.objects.get(id=id)
    if request.method == "POST":

        input_merek = request.POST.get('merek')
        input_nama = request.POST.get('nama')
        input_deskripsi = request.POST.get('deskripsi')
        input_harga = request.POST.get('harga')

        get_merek = Merek.objects.get(nama=input_merek)

        get_produk.nama = input_nama
        get_produk.deskripsi = input_deskripsi
        get_produk.harga = input_harga
        get_produk.merek = get_merek
        get_produk.save()
        return redirect(mobil_list)
    context = {
        'title':'Halaman Tambah Barang',
        'merek':merek,
        'get_produk':get_produk,
    }
    return render(request, template_name, context)

def mobil_delete(request, id):
    Produk.objects.get(id=id).delete()
    return redirect(mobil_list)


    