# Generated by Django 3.1.5 on 2021-03-03 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_auto_20210303_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='_cpf',
            field=models.CharField(db_column='cpf', help_text='Nº do CPF da pessoa.', max_length=11, unique=True, verbose_name='Nº CPF'),
        ),
    ]
