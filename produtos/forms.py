from django import forms
from .models import Produto
from .services.suppliers import SupplierAPI

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'preco', 'fornecedor_id']   # ← importante

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        suppliers = SupplierAPI.get_suppliers()

        choices = [('', 'Selecione um fornecedor...')]
        for supplier in suppliers:
            choices.append((
                supplier['id'],
                supplier['nome_empresa']
            ))

        # Força a criação do campo se não existir
        if 'fornecedor_id' not in self.fields:
            self.fields['fornecedor_id'] = forms.ChoiceField()

        self.fields['fornecedor_id'].widget = forms.Select(
            choices=choices,
            attrs={'class': 'form-control'}
        )
        self.fields['fornecedor_id'].label = "Fornecedor"
        self.fields['fornecedor_id'].required = False