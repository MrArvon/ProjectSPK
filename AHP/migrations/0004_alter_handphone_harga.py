# Generated by Django 4.0.4 on 2022-04-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AHP', '0003_design_alter_handphone_design'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handphone',
            name='harga',
            field=models.FloatField(),
        ),
    ]
