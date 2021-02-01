from django.db import models

PIZZA_CHOICES = (
    ('americano', 'Americano'),
    ('italiano', 'Italiano'),
)


class PizzaSize(models.Model):
    size = models.CharField('size', choices=PIZZA_CHOICES, default='americano', max_length=10)
    slug = models.SlugField('slug', choices=PIZZA_CHOICES, default='Americano')

    def __str__(self):
        return self.size


class Pizza(models.Model):
    size = models.ManyToManyField(PizzaSize, verbose_name="size.pizza")
    title = models.CharField('Name pizza', max_length=50, unique=True)
    content = models.TextField('Content Pizza')
    price = models.PositiveIntegerField('Price pizza')

    def __str__(self):
        return self.title

