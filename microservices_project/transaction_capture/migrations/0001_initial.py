# Generated by Django 4.2.1 on 2023-05-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('identificacion', models.CharField(max_length=20)),
                ('concepto_pago', models.CharField(max_length=100)),
                ('sede', models.CharField(max_length=100)),
                ('monto_compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medio_pago', models.CharField(max_length=100)),
                ('franquicia', models.CharField(max_length=100)),
                ('numero_cuotas', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('numero_transaccion', models.CharField(max_length=100)),
                ('exitoso', models.BooleanField(default=False)),
            ],
        ),
    ]
