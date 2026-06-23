from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'produtos', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('api/produtos', ProdutoViewSet.as_view(), name='api-listar-produtos'),
    path('listarprodutos', views.listarProdutos),
    path('cadastroProduto', views.cadastroProduto),
    path('excluirProduto/<int:id>', views.excluirProduto),
    path('editarProduto/<int:id>', views.editarProduto),
    path('login', views.formlogin),
    path('logout', views.logout_view)
]

urlpatterns += router.urls