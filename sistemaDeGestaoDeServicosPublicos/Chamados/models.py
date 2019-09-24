from django.db import models
from django.contrib.auth.models import User
from Orgao.models import Orgao
from Usuario.models import Endereco
from datetime import datetime
from random import randint


class TipoChamado(models.Model):
    descricaoTipoChamado = models.CharField('TIPO CHAMADO', max_length=45)
    idOrgao = models.ForeignKey(
        Orgao, on_delete=models.CASCADE, verbose_name="ORGÃO")

    def __str__(self):
        return self.descricaoTipoChamado

    class Meta:
        verbose_name = "TipoChamados"
        verbose_name_plural = "TipoChamados"

class Status(models.Model):
    descricao = models.CharField('DESCRIÇÃO', max_length=45)
    
    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

class OcorrenciasChamado(models.Model):
    descricaoOcorrenciasChamado = models.CharField('DESCRIÇÃO DE OCORRENCIAS DE CHAMADO', max_length=45)
    idChamado = models.ForeignKey(
        'Chamado', on_delete=models.CASCADE, verbose_name="CHAMADO",  default="")
    
    def __str__(self):
        return self.descricaoOcorrenciasChamado

    class Meta:
        verbose_name = "OcorrenciasChamado"
        verbose_name_plural = "OcorrenciasChamado"

class Chamado(models.Model):
    dataAbertura = models.DateField('ABERTO EM',auto_now_add=True)
    dataConclusao = models.DateField('CONCLUÍDO EM',auto_now=True)
    numeroProtocolo = models.CharField('NÚMERO DE PROTOCOLO', max_length=45, null=True, blank=True)
    observacao = models.CharField('OBSERVAÇÃO',max_length=100)
    observacaoOrgao = models.CharField('RETORNO DO ÓRGÃO', max_length=100, null=True, blank=True)
    idStatus = models.ForeignKey(
        Status, on_delete=models.CASCADE, verbose_name="STATUS")
    idOrgao = models.ForeignKey(
        Orgao, on_delete=models.CASCADE, verbose_name="ORGÃO")
    idTipoChamado = models.ForeignKey(
        TipoChamado, on_delete=models.CASCADE, verbose_name="TIPO DE CHAMADO")
    idUsuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="USUÁRIO")
    idEndereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, verbose_name="ENDEREÇO DO CHAMADO")
    

    
    def __str__(self):
        return self.observacao

    class Meta:
        verbose_name = "Chamado"
        verbose_name_plural = "Chamados"

    def gerarProtocolo(*args, **kwargs):
        now = datetime.now()
        ano = now.year
        mes = now.month
        dia = now.day
        horas = now.hour
        minutos = now.minute
        segundos = now.second
        aleatorio = (randint(0,9)* segundos)
        protocolo =  '{}{}{}{}{}{}{}'.format(ano,mes,dia,horas,minutos,segundos,aleatorio)
        return protocolo

