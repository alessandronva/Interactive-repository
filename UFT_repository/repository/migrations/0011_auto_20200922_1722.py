# Generated by Django 2.2 on 2020-09-22 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0010_auto_20200824_0139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Trabajo'},
        ),
        migrations.AlterModelOptions(
            name='tutor',
            options={'verbose_name': 'Tutor', 'verbose_name_plural': 'Tutores'},
        ),
    ]
