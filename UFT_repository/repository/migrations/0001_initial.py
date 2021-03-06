# Generated by Django 2.2 on 2020-07-31 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=20, verbose_name='Apellido')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True, verbose_name='Titulo')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('special_mention', models.BooleanField(verbose_name='Mencion especial')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='repository.Tutor')),
            ],
        ),
    ]
