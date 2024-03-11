from django.db import models
from django.utils.timezone import datetime


# Create your models here.
class ExemploModel(models.Model):
    # Campos de texto
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Campos numéricos
    age = models.IntegerField()
    height = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Campos de data e hora
    # Campos booleanos
    is_active = models.BooleanField()

    # Campos de chave estrangeira
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey('auth.Group', on_delete=models.PROTECT)

    # Campos de escolha
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    # Campos de arquivos
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')

    # Campos de endereço
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)


