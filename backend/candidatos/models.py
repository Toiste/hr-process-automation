from django.db import models

# Create your models here.

class Candidato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    experiencia = models.TextField()
    formacao = models.TextField()
    pontuacao = models.FloatField()
    vaga = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.vaga}"
