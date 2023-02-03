from django.contrib import admin
from .models import Endereco

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'logradouro',
        'cidade',
        'estado',
        'pais',
        ]

    search_fields = [
        'id',
        'logradouro',
        'cidade',
        'estado',
        'pais',
            
        ]

    list_filter = [
        'id',
        'logradouro',
        'cidade',
        'estado',
        'pais',
            
        ]