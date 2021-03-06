from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

# Create your models here.


def validate_pdf(file):
    if not str(file).endswith('.pdf'):
        raise ValidationError(gettext_lazy('Debe ser un archivo PDF'))

class Tutor(models.Model):
    name = models.CharField(verbose_name="Nombre y Apellido", max_length=50)

    class Meta:
        verbose_name = "Tutor"
        verbose_name_plural = "Tutores"

    def __str__(self):
        return f"{self.name}"

class Project(models.Model):
    title = models.TextField(verbose_name="Titulo", unique=True, max_length=300)
    description = models.TextField(verbose_name='Resumen')
    author = models.CharField(verbose_name='Autor', max_length=60)
    date = models.DateField(verbose_name="Fecha")
    tutor = models.ForeignKey(to=Tutor, on_delete=models.CASCADE)
    special_mention = models.BooleanField(verbose_name="Mencion especial")
    file = models.FileField(verbose_name="Archivo PDF", upload_to='./files', validators=(validate_pdf,))

    class Meta:
        verbose_name = "Trabajo"

    def __str__(self):
        return self.title