# Generated by Django 5.0.3 on 2024-03-25 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planilla', '0003_presupuesto_fecha_presupuesto_manodeobra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='precio',
            field=models.PositiveSmallIntegerField(max_length=12, verbose_name='PrecioTotal'),
        ),
    ]
