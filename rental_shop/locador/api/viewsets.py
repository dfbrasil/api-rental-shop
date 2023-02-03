from rest_framework.viewsets import ModelViewSet
from rental_shop.locador.models import Locador
from .serializers import LocadorSerializer


class LocadorViewSet(ModelViewSet):
    queryset = Locador.objects.all()
    serializer_class = LocadorSerializer
    # filterset_fields = ['carrinho']

