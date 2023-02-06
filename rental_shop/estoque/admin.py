from django.contrib import admin

from .models import Estoque

@admin.register(Estoque)

class EstoqueAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        ]

    # search_fields = [
    #     'id',
    #     'nome',
    #     'preco',
    #     ]

    # list_filter = [
    #     'id',
    #     'nome',
    #     'preco',
    #     'quantidade'
            
    #     ]

    readonly_fields = [
        'lista_itens',
    ]