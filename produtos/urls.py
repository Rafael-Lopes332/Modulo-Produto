from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'api/produtos', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('api/produtos', ProdutoViewSet.as_view({'get': 'list', 'post': 'create'}), name='api-produtos-lista-criar'),
    path('api/produtos/<int:pk>', ProdutoViewSet.as_view({
        'get': 'retrieve', 
        'put': 'update', 
        'patch': 'partial_update', 
        'delete': 'destroy'
    }), name='api-produtos-detalhe-alterar-excluir'),

    path('listarprodutos', views.listarProdutos),
    path('cadastroProduto', views.cadastroProduto),
    path('excluirProduto/<int:id>', views.excluirProduto),
    path('editarProduto/<int:id>', views.editarProduto),
    path('login', views.formlogin),
    path('logout', views.logout_view)
]

urlpatterns += router.urls