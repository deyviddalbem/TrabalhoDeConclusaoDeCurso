# Generated by Django 2.2.4 on 2019-08-23 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTelefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=20, verbose_name='TIPO TELEFONE')),
            ],
            options={
                'verbose_name': 'TipoTelefone',
                'verbose_name_plural': 'TipoTelefones',
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=11, verbose_name='NÚMERO')),
                ('idPessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='PESSOA')),
                ('idTipoTelefone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.TipoTelefone', verbose_name='TIPO TELEFONE')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.IntegerField(verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=45, verbose_name='LOGRADOURO')),
                ('enderecoNumero', models.CharField(max_length=11, verbose_name='NÚMERO')),
                ('complemento', models.CharField(max_length=45, verbose_name='COMPLEMENTO')),
                ('bairro', models.CharField(max_length=45, verbose_name='BAIRRO')),
                ('observacao', models.CharField(max_length=45, verbose_name='OBSERVAÇÃO')),
                ('municipio', models.CharField(max_length=45, verbose_name='MUNICIPIO')),
                ('estado', models.CharField(max_length=2, verbose_name='ESTADO')),
                ('idPessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='PESSOA')),
            ],
            options={
                'verbose_name': 'Endereco',
                'verbose_name_plural': 'Endereco',
            },
        ),
    ]
