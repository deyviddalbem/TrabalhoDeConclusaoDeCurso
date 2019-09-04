from django.db import models
from django.contrib.auth.models import User
from Orgao.models import Orgao

class TipoChamado(models.Model):
    descricaoTipoChamado = models.CharField('TIPO CHAMADO', max_length=45)
    idOrgao = models.ForeignKey(
        Orgao, on_delete=models.CASCADE, verbose_name="ORGÃO")

    def __str__(self):
        return self.descricaoTipoChamado

    class Meta:
        verbose_name = "TipoChamados"
        verbose_name_plural = "TipoChamados"