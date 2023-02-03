from rest_framework.viewsets import ModelViewSet
from item.models import Item
from .serializers import ItemSerializer

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer