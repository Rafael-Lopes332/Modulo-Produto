from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    categoria = models.CharField(max_length=100, verbose_name="Categoria")
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Preço"
    )

    fornecedor_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Fornecedor"
    )

    def __str__(self):
        return self.nome

    def get_fornecedor_nome(self):
        from .services.suppliers import SupplierAPI
        return SupplierAPI.get_supplier_name(self.fornecedor_id)