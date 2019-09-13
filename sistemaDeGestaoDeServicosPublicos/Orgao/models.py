from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from Usuario.models import Endereco, Telefone



class Orgao(models.Model):
    nomeOrgao = models.CharField('NOME ORGÃO', max_length=45)
    descricao = models.CharField('DESCRIÇÃO', max_length=100)
    emailOrgao = models.CharField('EMAIL ORGÃO', max_length=45)
    nomeResponsavelOrgao = models.CharField(
        'RESPONSÁVEL PELO ÓRGÃO', max_length=45)
    enderecoOrgao = models.CharField('ENDERECO ORGÃO', max_length=45, default="")
    telefoneOrgao = models.IntegerField('TELEFONE ORGÃO')
    

    def __str__(self):
        return self.nomeOrgao

    class Meta:
        verbose_name = "Orgao"
        verbose_name_plural = "Orgao"


class TipoLotacao(models.Model):
    descricao = models.CharField('DESCRIÇÃO', max_length=45)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "TipoLotacao"
        verbose_name_plural = "TiposLotacao"


class Lotacao(models.Model):
    observacao = models.CharField('OBSERVAÇÃO', max_length=45)
    idTipoLotacao = models.ForeignKey(
        TipoLotacao, on_delete=models.CASCADE, verbose_name="TIPO LOTAÇÃO")
    idUsuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="USUÁRIO")
    idOrgao = models.ForeignKey(
        Orgao, on_delete=models.CASCADE, verbose_name="ÓRGÃO")

    def __str__(self):
        return self.idUsuario.first_name + " - " + self.idTipoLotacao.descricao 

    class Meta:
        verbose_name = "Lotacao"
        verbose_name_plural = "Lotacao"