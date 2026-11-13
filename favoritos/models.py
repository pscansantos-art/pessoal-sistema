from django.db import models

class Favorito(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50) # Ex: Filme, Música, Banda
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} ({self.categoria})"