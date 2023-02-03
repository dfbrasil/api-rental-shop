from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'nome',
        'preco',
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
            
        ]
