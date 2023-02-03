from rest_framework.viewsets import ModelViewSet
from usuario.models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # filterset_fields = ['nome']

