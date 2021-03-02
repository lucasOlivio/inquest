# Generated by Django 3.1.5 on 2021-03-02 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome da pessoa.', max_length=255, verbose_name='Nome')),
                ('cpf', models.CharField(help_text='Nº do CPF da pessoa.', max_length=14, verbose_name='Nº CPF')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de criação')),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now, help_text='Data da ultima atualização da pessoa.', verbose_name='Data da atualização')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'ordering': ['-date_created'],
            },
        ),
    ]
