from django.db import models
'''from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.
class StockItems(models.Model):
    item = models.CharField(verbose_name='Item', max_length=15)
    value = models.IntegerField(verbose_name='Valor do Item')

    class Meta:
        verbose_name = 'Item de Estoque'
        verbose_name_plural = 'Itens de Estoque'
    
    def __str__(self):
        return self.item

    
    TYPE_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    owner = models.ForeignKey(User, verbose_name='Sobrevivente', on_delete=models.CASCADE)
    idade = models.IntegerField(verbose_name='Idade')
    gender = models.CharField(verbose_name='Sexo', max_length=50, choices=TYPE_CHOICES)
'''