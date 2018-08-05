"""
Definition of models.
"""

from django.db import models

class Participantes(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    empresa = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    area_atuacao = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="upload/images/")

