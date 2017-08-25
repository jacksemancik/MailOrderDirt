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
    about_one = models.TextField()
    about_two = models.TextField()
    def __str__(self):
        return self.about_one

class Skills(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.title

class ContactModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.email
