from django.db import models
from django.urls import reverse

# Create your models here.


class Cuenta(models.Model):
    id_cuenta = models.AutoField(primary_key=True)
    name_cuenta = models.CharField(max_length=50,
                                   verbose_name="Cuenta",
                                   blank=False,
                                   null=False,
                                   help_text="Ingresa el nombre de la cuenta.")

    description_cuenta = models.TextField(max_length=500,
                                          verbose_name="Descripción de la cuenta",
                                          null=True,
                                          default="Agrega una descripción a tu cuenta.",
                                          help_text="Tomate tu tiempo e ingresa una buena descripción")

    LOAN_STATUS = (
        (True, "Activo"),
        (False, "Inactivo")
    )

    status_cuenta = models.BooleanField(verbose_name="Estado",
                                        default=True,
                                        null=True,
                                        blank=True,
                                        choices=LOAN_STATUS,
                                        help_text="Ingrese un estado para la cuenta.")

    date_since = models.DateTimeField(verbose_name="Fecha de Actividad.",
                                      blank=True,
                                      null=True,
                                      help_text="Ingrese la fecha de actividad para la cuenta.")

    date_until = models.DateTimeField(verbose_name="Fecha de Inactividad",
                                      blank=True,
                                      null=True,
                                      help_text="Ingrese la fecha de inactividad para la cuenta.")

    def __str__(self):

        return self.name_cuenta

    # def get_absolute_url(self):
    #     return reverse('cuenta-detail', args=[str(self.id_cuenta)])


class SalesAccountTrimester(models.Model):

    account = models.CharField(max_length=50, null=True, blank=True)
    year = models.SmallIntegerField(null=True, blank=True)
    trimester = models.SmallIntegerField(null=True, blank=True)
    sales = models.SmallIntegerField(null=True, blank=True)
    filename = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.account

    # def get_absolute_url(self):
    #     return reverse('salesaccounttrimester-detail', args=[str(self.account)])
