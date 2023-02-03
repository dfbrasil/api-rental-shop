from django.contrib import admin
from .models import ItemPedido

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'item',
        'quantidade',
        ]

    search_fields = [
        'id',
        'item',
        'quantidade',
            
        ]

    list_filter = [
        'id',
        'item',
        'quantidade',
            
        ]