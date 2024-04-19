from django.db import models

class Tenis(models.Model):
    TYPE_CHOICES = (
        ('Correr', 'Correr'),
        ('Casuales', 'Casuales'),
        ('Bota', 'Bota'),
    )
    BRAND_CHOICES = (
        ('Nike', 'Nike'),
        ('Adidas', 'Adidas'),
        ('Pirma', 'Pirma'),
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)

    def __str__(self):
        return f"{self.brand} {self.name}"
