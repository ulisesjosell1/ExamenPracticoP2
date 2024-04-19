# Generated by Django 5.0.3 on 2024-04-19 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0006_producto_delete_tenis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(choices=[('Running precision VI', 'Running precision VI'), ('BrandNewElegant', 'BrandNewElegant'), ('Los del CR7', 'Los del CR7')], max_length=50)),
                ('type', models.CharField(choices=[('Correr', 'Correr'), ('Casuales', 'Casuales'), ('Bota', 'Bota')], max_length=50)),
                ('brand', models.CharField(choices=[('Nike', 'Nike'), ('Adidas', 'Adidas'), ('Pirma', 'Pirma')], max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
