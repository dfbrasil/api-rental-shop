from rest_framework.serializers import ModelSerializer
from item.models import Item

class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = ['id','nome','preco','disponivel']