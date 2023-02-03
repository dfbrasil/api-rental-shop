from rest_framework.viewsets import ModelViewSet
from rental_shop.locatario.models import Locatario
from .serializers import LocatarioSerializer


class LocatarioViewSet(ModelViewSet):
    queryset = Locatario.objects.all()
    serializer_class = LocatarioSerializer
    # filterset_fields = ['usuario']

