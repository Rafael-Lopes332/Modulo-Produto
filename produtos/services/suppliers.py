import requests
from django.core.cache import cache
from django.conf import settings

class SupplierAPI:
    BASE_URL = "https://wanderson020.pythonanywhere.com/api"

    @classmethod
    def get_suppliers(cls):
        cache_key = "suppliers_list"
        suppliers = cache.get(cache_key)

        if suppliers is None:
            try:
                response = requests.get(
                    f"{cls.BASE_URL}/fornecedores/",
                    timeout=10,
                    headers={
                        "Accept": "application/json",
                    }
                )
                response.raise_for_status()
                suppliers = response.json()
                cache.set(cache_key, suppliers, 300)
            except Exception as e:
                print(f"Erro ao buscar fornecedores: {e}")
                suppliers = []
        return suppliers

    @classmethod
    def get_supplier_name(cls, supplier_id):
        if not supplier_id:
            return "—"
        try:
            suppliers = cls.get_suppliers()
            for supplier in suppliers:
                if str(supplier.get('id')) == str(supplier_id):
                    return supplier.get('nome_empresa', 'Sem nome')
            return "Fornecedor não encontrado"
        except:
            return "Erro ao carregar fornecedor"