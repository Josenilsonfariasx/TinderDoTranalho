# Generated by Django 4.0.6 on 2022-08-10 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_remove_usuario_idade_usuario_pretencao_salarial'),
        ('vagas', '0011_alter_vagas_escolaridade_alter_vagas_faixa_salarial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='candidatos',
            field=models.ManyToManyField(related_name='Vagas', to='usuario.usuario'),
        ),
    ]
