# Generated by Django 2.2 on 2020-09-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre y apellido', max_length=50, verbose_name='Nombre')),
                ('img', models.ImageField(help_text='(200X300px recomendado)', upload_to='./media/', verbose_name='Foto')),
                ('role', models.CharField(choices=[('admin', 'Administrativo'), ('prof', 'Profesor'), ('boss', 'Jefe')], max_length=50, verbose_name='Puesto')),
                ('status', models.BooleanField(verbose_name='Personal activo')),
            ],
        ),
    ]