# Generated by Django 5.0.3 on 2024-03-28 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planilla', '0005_presupuesto_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuesto',
            name='done',
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='manoDeObra',
            field=models.IntegerField(max_length=33),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='materiaPrima',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='precio',
            field=models.IntegerField(max_length=12, verbose_name='PrecioTotal'),
        ),
    ]
