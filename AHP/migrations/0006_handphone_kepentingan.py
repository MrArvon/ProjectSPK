# Generated by Django 4.0.4 on 2022-04-26 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AHP', '0005_kepentingan'),
    ]

    operations = [
        migrations.AddField(
            model_name='handphone',
            name='kepentingan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AHP.kepentingan'),
        ),
    ]
