# Generated by Django 2.2 on 2020-10-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20200923_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='img',
            field=models.ImageField(blank=True, help_text='(200X300px recomendado)', null=True, upload_to='employees', verbose_name='Foto'),
        ),
    ]
