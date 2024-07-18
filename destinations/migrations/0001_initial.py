# Generated by Django 5.0.6 on 2024-07-18 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidade',
            fields=[
                ('cnpj', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('razaosocial', models.CharField(max_length=50)),
                ('nf', models.CharField(max_length=50)),
                ('contatos', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('fones', models.CharField(max_length=35)),
                ('validade', models.DateField()),
                ('ativo', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroLancamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Lancamento',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('tipo_saida', models.CharField(max_length=2)),
                ('produto', models.CharField(max_length=60)),
                ('marca', models.CharField(max_length=50)),
                ('qn', models.CharField(max_length=10)),
                ('unid', models.CharField(default=None, max_length=5)),
                ('quant', models.SmallIntegerField()),
                ('cnpj', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='destinations.entidade')),
            ],
        ),
    ]
