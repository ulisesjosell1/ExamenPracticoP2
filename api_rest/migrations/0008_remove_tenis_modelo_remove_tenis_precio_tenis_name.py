# Generated by Django 5.0.3 on 2024-04-19 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0007_tenis_delete_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenis',
            name='Modelo',
        ),
        migrations.RemoveField(
            model_name='tenis',
            name='precio',
        ),
        migrations.AddField(
            model_name='tenis',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
