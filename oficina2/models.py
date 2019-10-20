from django.db import models

# Create your models here.
class Orcamento(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente = models.CharField(max_length=50)
    datahora = models.DateTimeField()
    descricao = models.TextField()
    valor = models.FloatField()
    vendedor = models.CharField(max_length=50)

    def __str__(self):
        return f'ID:{self.id} Cliente: {self.cliente.capitalize()} Valor:{self.valor} Descrição: {self.descricao[0:50].capitalize()}'
        

