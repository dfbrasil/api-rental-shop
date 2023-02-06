from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'nome',
        'preco',
        'quantidade',
        'disponivel',
        ]

    search_fields = [
        'id',
        'nome',
        'preco',
        ]

    list_filter = [
        'id',
        'nome',
        'preco',
        'quantidade'
            
        ]

    readonly_fields = [
        'quantidade_restante',
    ]
