from django.db import models

# Create your models here.

class Merek(models.Model):
    nama = models.CharField(max_length=40)
    def __str__(self):
        return self.nama

class Produk(models.Model):
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField()
    harga = models.IntegerField()
    merek = models.ForeignKey(Merek, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.nama 
