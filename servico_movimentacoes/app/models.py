from django.db import models
from django.utils import timezone

class Movimentacao(models.Model):
    produto_id = models.IntegerField()
    setor_origem_id = models.IntegerField()
    setor_destino_id = models.IntegerField()
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(default=timezone.now)