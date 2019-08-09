from django.db import models
from django.contrib.auth.models import User


class TipoTelefone(models.Model):
    descricao = models.CharField('TIPO TELEFONE', max_length=20)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "TipoTelefone"
        verbose_name_plural = "TipoTelefones"

class Telefone(models.Model):
    numero = models.CharField('NÚMERO', max_length=11)
    idTipoTelefone = models.ForeignKey(
        TipoTelefone, on_delete=models.CASCADE, verbose_name="TIPO TELEFONE")
    idPessoa = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="PESSOA")

    def __str__(self):
        return self.idPessoa.first_name + " - " + self.numero


    class Meta:
        verbose_name = "Telefone"
        verbose_name_plural = "Telefones"

class Estado(models.Model):
    nomeEstado = models.CharField('NOME ESTADO', max_length=20)

    def __str__(self):
        return self.nomeEstado

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

class Municipio(models.Model):
    nomeMunicipio = models.CharField('NOME MUNICIPIO', max_length=20)
    idEstado = models.ForeignKey(
        Estado, on_delete=models.CASCADE, verbose_name="NOME ESTADO")

    def __str__(self):
        return self.nomeMunicipio
    
    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

class Bairro(models.Model):
    nomeBairro = models.CharField('NOME BAIRRO', max_length=20)
    idMunicipio = models.ForeignKey(
        Municipio, on_delete=models.CASCADE, verbose_name="NOME MUNICIPIO")

    def __str__(self):
        return self.nomeBairro


    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"

class Rua(models.Model):
    cepRua = models.CharField('CEP RUA', max_length=20)
    nomeRua = models.CharField('NOME RUA', max_length=20)
    idBairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, verbose_name="NOME BAIRRO")

    def __str__(self):
        return self.cepRua + self.nomeRua + self.idBairro.nomeBairro  


    class Meta:
        verbose_name = "Rua"
        verbose_name_plural = "Ruas"