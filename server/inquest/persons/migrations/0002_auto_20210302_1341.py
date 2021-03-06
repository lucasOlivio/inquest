# Generated by Django 3.1.5 on 2021-03-02 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='user_created',
            field=models.ForeignKey(help_text='Criador da pessoa.', on_delete=django.db.models.deletion.CASCADE, related_name='persons_created', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AddField(
            model_name='person',
            name='user_updated',
            field=models.ForeignKey(blank=True, help_text='Último usuário que atualizou a pessoa.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='persons_updated', to=settings.AUTH_USER_MODEL, verbose_name='Ultimo atualizador'),
        ),
    ]
