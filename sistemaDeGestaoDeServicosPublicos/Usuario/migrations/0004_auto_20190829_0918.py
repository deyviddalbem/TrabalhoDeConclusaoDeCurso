# Generated by Django 2.2.4 on 2019-08-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0003_auto_20190826_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.IntegerField(verbose_name='CEP'),
        ),
    ]