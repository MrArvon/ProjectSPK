# Generated by Django 4.0.4 on 2022-05-04 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AHP', '0008_nilai_penting_rename_nama_kepentingan_kategori_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='kepentingan',
        ),
        migrations.DeleteModel(
            name='nilai_penting',
        ),
    ]