from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Le modèle Adress est lié au modèle de Letting (location).
    La class Meta est utilisée pour régulariser l'orthographe de Adress au
    pluriel dans le site d'administration de Django
    """
    class Meta:
        verbose_name = "Adress"
        verbose_name_plural = "Adresses"
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)]
    )
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"


class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
