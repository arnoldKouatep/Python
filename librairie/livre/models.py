from django.db import models

# Create your models here.
class Livre(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=60)
    prix = models.FloatField(default=0)
    description = models.TextField(null=True)