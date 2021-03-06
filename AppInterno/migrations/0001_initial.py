# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 22:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataIncepere', models.DateField(null=True)),
                ('dataExpirare', models.DateField(null=True)),
                ('obligatii', models.CharField(max_length=6000)),
                ('dataEmitereFactura', models.DateField(null=True)),
                ('tipCopie', models.BooleanField()),
                ('modTrimitere', models.BooleanField()),
                ('semnat', models.BooleanField()),
                ('dataPlata', models.DateField(max_length=20)),
                ('dataRapAct', models.DateField(max_length=20)),
                ('dataRapInter', models.DateField(max_length=20)),
                ('numefis', models.CharField(max_length=100)),
                ('extensie', models.CharField(max_length=20))
            ],
        ),
        migrations.CreateModel(
            name='ContractCustom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=6000)),
            ],
        ),
        migrations.CreateModel(
            name='Furnizor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Modificare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataModificare', models.DateTimeField(null=True)),
                ('dataIncepereBefore', models.DateField(null=True)),
                ('dataIncepereAfter', models.DateField(null=True)),
                ('dataExpirareBefore', models.DateField(null=True)),
                ('dataExpirareAfter', models.DateField(null=True)),
                ('obligatiiBefore', models.CharField(max_length=6000, null=True)),
                ('obligatiiAfter', models.CharField(max_length=6000, null=True)),
                ('dataEmitereFacturaBefore', models.DateField(null=True)),
                ('dataEmitereFacturaAfter', models.DateField(null=True)),
                ('tipCopieBefore', models.NullBooleanField()),
                ('tipCopieAfter', models.NullBooleanField()),
                ('modTrimitereBefore', models.NullBooleanField()),
                ('modTrimitereAfter', models.NullBooleanField()),
                ('semnatBefore', models.NullBooleanField()),
                ('semnatAfter', models.NullBooleanField()),
                ('dataPlataBefore', models.DateField(max_length=20, null=True)),
                ('dataPlataAfter', models.DateField(max_length=20, null=True)),
                ('dataRapActBefore', models.DateField(max_length=20, null=True)),
                ('dataRapActAfter', models.DateField(max_length=20, null=True)),
                ('dataRapInterBefore', models.DateField(max_length=20, null=True)),
                ('dataRapInterAfter', models.DateField(max_length=20, null=True)),
                ('numefisBefore', models.CharField(max_length=100, null=True)),
                ('numefisAfter', models.CharField(max_length=100, null=True)),
                ('extensieBefore', models.CharField(max_length=20, null=True)),
                ('extensieAfter', models.CharField(max_length=20, null=True)),
                ('tip', models.CharField(max_length=20, null=True)),
                ('idContract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppInterno.Contract')),
            ],
        ),
        migrations.CreateModel(
            name='ModificareCustom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textBefore', models.CharField(max_length=6000)),
                ('textAfter', models.CharField(max_length=6000)),
                ('idContract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppInterno.ContractCustom')),
            ],
        ),
        migrations.AddField(
            model_name='modificarecustom',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.User'),
        ),
        migrations.AddField(
            model_name='modificare',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.User'),
        ),
        migrations.AddField(
            model_name='contract',
            name='idFurnizor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppInterno.Furnizor'),
        ),
    ]
