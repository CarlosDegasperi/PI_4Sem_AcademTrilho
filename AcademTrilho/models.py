from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        app_label = 'AcademTrilho'

    def __str__(self):
        return self.nome

class Semestre(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
