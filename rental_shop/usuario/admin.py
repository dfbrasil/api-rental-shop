from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'nome',
        'cpf_cnpj',
        'tipo',
        'email',
        'senha',
        'endereco',
        
        ]

    search_fields = [
        'id',
        'nome',
        'cpf_cnpj',
        'tipo',
        'email',
        'senha',
        'endereco',
            
        ]

    list_filter = [
        'id',
        'nome',
        'cpf_cnpj',
        'tipo',
        'email',
        'senha',
        'endereco',
            
        ]
