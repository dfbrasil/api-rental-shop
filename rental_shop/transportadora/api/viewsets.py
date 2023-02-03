from rest_framework.viewsets import ModelViewSet
from transportadora.models import Transportadora
from .serializers import TransportadoraSerializer


class TransportadoraViewSet(ModelViewSet):
    queryset = Transportadora.objects.all()
    serializer_class = TransportadoraSerializer
    # filterset_fields = ['nome']

