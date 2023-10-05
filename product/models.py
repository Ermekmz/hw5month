from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


# Create your models here
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Review(models.Model):
    text = models.TextField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1, blank=True)

    def __str__(self):
        return f'{self.text}'
