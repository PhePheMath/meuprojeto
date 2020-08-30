from django.db import models

class Enquetes(models.Model):

    nome = models.CharField(null=True, blank=True, max_length=80)
    idade = models.IntegerField(null=True, blank=True)
    enquete = models.TextField(null=True, blank=True)