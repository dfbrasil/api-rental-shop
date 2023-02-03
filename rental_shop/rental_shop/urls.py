from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rental_shop.carrinho.api.viewsets import CarrinhoViewSet
from rental_shop.endereco.api.viewsets import EnderecoViewSet
# from rental_shop.estoque.api.viewsets import EstoqueViewSet
from rental_shop.item.api.viewsets import ItemViewSet
from rental_shop.item_pedido.api.viewsets import ItemPedidoViewSet
from rental_shop.locador.api.viewsets import LocadorViewSet
from rental_shop.locatario.api.viewsets import LocatarioViewSet
from rental_shop.transportadora.api.viewsets import TransportadoraViewSet
from rental_shop.usuario.api.viewsets import UsuarioViewSet
# from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'carrinhos', CarrinhoViewSet)
router.register(r'enderecos', EnderecoViewSet)
# router.register(r'estoques', EstoqueViewSet)
router.register(r'itens', ItemViewSet)
router.register(r'itemPedidos', ItemPedidoViewSet)
router.register(r'locadores', LocadorViewSet)
router.register(r'locatarios', LocatarioViewSet)
router.register(r'transportadoras', TransportadoraViewSet)
router.register(r'usuarios', UsuarioViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    # path('api-token-auth/', obtain_auth_token),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

