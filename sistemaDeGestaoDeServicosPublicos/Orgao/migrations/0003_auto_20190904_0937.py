# Generated by Django 2.2.4 on 2019-09-04 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orgao', '0002_auto_20190903_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgao',
            name='idTipoChamado',
        ),
        migrations.AlterField(
            model_name='lotacao',
            name='observacao',
            field=models.CharField(max_length=45, verbose_name='OBSERVAÇÃO'),
        ),
    ]
