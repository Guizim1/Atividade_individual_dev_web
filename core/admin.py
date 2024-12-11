from django.contrib import admin
from .models import MestreDeJogo, Jogador

class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'mestre_de_jogo_nome')

    def mestre_de_jogo_nome(self, obj):
        return obj.mestre_de_jogo.nome  # Ajuste conforme o atributo do modelo MestreDeJogo
    mestre_de_jogo_nome.short_description = 'Mestre de Jogo'  # Título da coluna

admin.site.register(Jogador, JogadorAdmin)
