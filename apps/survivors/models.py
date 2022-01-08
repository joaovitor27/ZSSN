from django.db import models

# Create your models here.
class StockItems(models.Model):
    item = models.CharField(verbose_name='Item', max_length=15)
    value = models.IntegerField(verbose_name='Valor do Item')

    class Meta:
        verbose_name = 'Item de Estoque'
        verbose_name_plural = 'Itens de Estoque'
    
    def __str__(self):
        return self.item
