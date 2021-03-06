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
    numero = models.IntegerField('NÚMERO')
    idTipoTelefone = models.ForeignKey(
        TipoTelefone, on_delete=models.CASCADE, verbose_name="TIPO TELEFONE")
    idPessoa = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="PESSOA")

    def __str__(self):
        return(str(self.numero))
        #return self.numero, "- " , self.idPessoa.first_name

    class Meta:
        verbose_name = "Telefone"
        verbose_name_plural = "Telefones"




class Endereco(models.Model):
    cep = models.IntegerField('CEP')
    logradouro = models.CharField('LOGRADOURO', max_length=45)
    enderecoNumero = models.CharField('NÚMERO', max_length=11)
    complemento = models.CharField('COMPLEMENTO', max_length=45)
    bairro = models.CharField('BAIRRO', max_length=45)
    observacao = models.CharField('OBSERVAÇÃO', max_length=45)
    municipio = models.CharField('MUNICIPIO', max_length=45)
    estado = models.CharField('ESTADO', max_length=2)   
    idPessoa = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="PESSOA")
   
 
    def __str__(self):
        return (str (self.cep))+" - " + self.logradouro +" - "+ self.enderecoNumero + " - " + self.bairro

    class Meta:
        verbose_name = "Endereco"
        verbose_name_plural = "Endereco"

# class fotoUsuario(models.Model):
#     foto = models.ImageField(default='default.png',upload_to='fotosUsuario/')
#     idPessoa = models.ForeignKey(
#         User, on_delete=models.CASCADE, verbose_name="PESSOA")
