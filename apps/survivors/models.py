from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StockItems(models.Model):
    item = models.CharField(verbose_name='Item', max_length=15)
    value = models.IntegerField(verbose_name='Valor do Item')

    class Meta:
        verbose_name = 'Item de Estoque'
        verbose_name_plural = 'Itens de Estoque'
    
    def __str__(self):
        return self.item


class Sobreviventes(models.Model):
    TYPE_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    onwer = models.ForeignKey(User, verbose_name='Sobrevivente', on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name='Idade')
    gender = models.CharField(verbose_name='Sexo', max_length=50, choices=TYPE_CHOICES)

    lat = models.DecimalField(verbose_name='Latitude', max_digits=9, decimal_places=6)
    log = models.DecimalField(verbose_name='Logetude', max_digits=9, decimal_places=6)

    Status = models.BooleanField(verbose_name='Infequitado', default=False)

    class Meta:
        verbose_name = 'Sobrevivente'
        verbose_name_plural = 'Sobreviventes'

    def __str__(self):
        return self.onwer.username


class accusations(models.Model):
    survivors = models.ManyToManyField(Sobreviventes, verbose_name='Sobrevivente')
    numbercomplaints = models.IntegerField(verbose_name='Número de Denúncias')

    class Meta:
        verbose_name = 'Denúncia'
        verbose_name_plural = 'Denúncias'

    def __str__(self):
        return self.survivors


class inventory(models.Model):
    amount = models.IntegerField(verbose_name='Quantidade')
    item = models.ManyToManyField(StockItems, verbose_name='Item')
    survivors = models.ForeignKey(Sobreviventes, verbose_name='Sobreviventes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'inventário'
        verbose_name_plural = 'inventários'

    def __str__(self):
        return self.amount + '|' + self.item

