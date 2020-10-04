from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=50, help_text="Nombre y apellido")
    img = models.ImageField(
        verbose_name="Foto",
        help_text="(200X300px recomendado)",
        upload_to="employees",
        blank = True,
        null= True
    )
    role = models.CharField(
        verbose_name="Puesto",
        max_length=50, 
        choices=[
            ("admin", "Administrativo"), # 'Administrativo', 'Profesor', 'Jefe'
            ("prof", "Profesor"),
            ("boss", "Jefe")
            ]
        )
    status = models.BooleanField(verbose_name='Personal activo')

    class Meta:
        verbose_name = "Empleado"

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(verbose_name="Nombre", help_text="Identificador del contacto", max_length=50)
    email = models.EmailField(verbose_name="Email", help_text="Ejemplo@gmail.com", null=True, blank=True)
    phone = models.CharField(verbose_name="Telefono", help_text="0251-1234567", null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = "Contacto"

    def __str__(self):
        return self.name