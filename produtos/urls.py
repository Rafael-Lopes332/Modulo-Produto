from django.urls import path
from .import views

from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'api/produtos', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('api/produtos', ProdutoViewSet.as_view({'get': 'list'}), name='api-listar-produtos'),
    path('api/produtos', ProdutoViewSet.as_view({'post': 'create'}), name='api-criar-produto'),
    path('api/produtos/<int:pk>', ProdutoViewSet.as_view({'get': 'retrieve'}), name='api-detalhar-produto'),
    path('api/produtos/<int:pk>', ProdutoViewSet.as_view({'put': 'update'}), name='api-editar-produto'),
    path('api/produtos/<int:pk>', ProdutoViewSet.as_view({'patch': 'partial_update'}), name='api-atualizar-parcial-produto'),
    path('api/produtos/<int:pk>', ProdutoViewSet.as_view({'delete': 'destroy'}), name='api-excluir-produto'),

    path('listarprodutos', views.listarProdutos),
    path('cadastroProduto', views.cadastroProduto),
    path('excluirProduto/<int:id>', views.excluirProduto),
    path('editarProduto/<int:id>', views.editarProduto),
    path('login', views.formlogin),
    path('logout', views.logout_view)
]

urlpatterns += router.urls