# Generated by Django 5.0.3 on 2024-03-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planilla', '0007_alter_presupuesto_manodeobra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='precio',
            field=models.IntegerField(max_length=50, verbose_name='PrecioTotal'),
        ),
    ]
