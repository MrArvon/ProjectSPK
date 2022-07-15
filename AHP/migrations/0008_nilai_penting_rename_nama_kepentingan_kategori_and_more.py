# Generated by Django 4.0.4 on 2022-04-26 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AHP', '0007_remove_handphone_kepentingan'),
    ]

    operations = [
        migrations.CreateModel(
            name='nilai_penting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.IntegerField()),
                ('nama', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='kepentingan',
            old_name='nama',
            new_name='kategori',
        ),
        migrations.RemoveField(
            model_name='kepentingan',
            name='nilai',
        ),
        migrations.AddField(
            model_name='kepentingan',
            name='nilai_penting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AHP.nilai_penting'),
        ),
    ]