# Generated by Django 2.2 on 2020-08-24 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0009_auto_20200824_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='project',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Tutor'),
        ),
    ]