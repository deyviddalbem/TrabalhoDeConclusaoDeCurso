from django.db import models
from django.contrib.auth.models import User


class TipoChamado(models.Model):
    descricaoTipoChamado = models.CharField('TIPO CHAMADO', max_length=45)

    def __str__(self):
        return self.descricaoTipoChamado

    class Meta:
        verbose_name = "TipoChamados"
        verbose_name_plural = "TipoChamados"