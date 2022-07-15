from django.db import models


class design(models.Model):
    nilai = models.IntegerField()
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama


class peforma(models.Model):
    nilai = models.IntegerField()
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama


# class nilai_penting(models.Model):
#     nilai = models.IntegerField()
#     nama = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.nama


class kepentingan(models.Model):
    design = models.IntegerField()
    storage = models.IntegerField()
    harga = models.IntegerField()
    peforma = models.IntegerField()


class handphone(models.Model):
    merk = models.CharField(max_length=20)
    design = models.ForeignKey(design, on_delete=models.CASCADE, null=True)
    storage = models.IntegerField()
    harga = models.FloatField()
    peforma = models.ForeignKey(peforma, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.merk
