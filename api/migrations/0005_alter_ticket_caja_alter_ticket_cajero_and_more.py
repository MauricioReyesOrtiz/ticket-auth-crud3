# Generated by Django 4.1.4 on 2022-12-21 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_cliente_clientefecha_cliente_clientefechanac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='caja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.caja', verbose_name='Caja'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='cajero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cajero', verbose_name='Cajero'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='nroticket',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sucursal', verbose_name='Sucursal'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tipoAtencion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipoatencion', verbose_name='Tipoatencion'),
        ),
    ]
