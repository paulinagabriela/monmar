from django.db import models

class Oferta(models.Model):#{{{
    PLN = 10
    WALUTA_CHOICES = (
            (PLN, (u'PLN')),
            )

    #fields#{{{
    nazwa = models.CharField(max_length=200)
    opis = models.TextField()
    cena =  models.DecimalField(max_digits=16, decimal_places=2)
    waluta = models.CharField(choices=WALUTA_CHOICES, max_length=5)
    #}}}
#}}}
