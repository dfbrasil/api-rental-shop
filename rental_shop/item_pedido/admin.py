from django.contrib import admin

from .models import ItemPedido


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'item',
        'qtd',
        ]

    search_fields = [
        'id',
        'item',
        'qtd',
            
        ]

    list_filter = [
        'id',
        'item',
        'qtd',
            
        ]