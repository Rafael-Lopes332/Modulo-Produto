from django.db import models

class Produto(models.Model):
    nome =  models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    preco = models.FloatField(max_length=50)

    def __str__(self):
        return self.nome