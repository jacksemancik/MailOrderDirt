from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    button = models.TextField()
    image = models.ImageField()
    slug = models.SlugField()
    def __str__(self):
        return self.name
class About(models.Model):
    about = models.TextField()
    def __str__(self):
        return self.about

class Skills(models.Model):
    icon = CharField(max_length=50)
    title = CharField(max_length=50)
    description = TextField()
    def __str__(self):
        return self.title
