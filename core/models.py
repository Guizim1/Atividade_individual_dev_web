from django.db import models

class MestreDeJogo(models.Model):
    nome = models.CharField(max_length=100)
    experiencia = models.TextField()
    
    def __str__(self):
        return self.nome

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    nivel = models.IntegerField()
    mestre_de_jogo = models.ForeignKey(MestreDeJogo, on_delete=models.CASCADE)  # Alterei o nome aqui para mestre_de_jogo

    def __str__(self):
        return self.nome

    