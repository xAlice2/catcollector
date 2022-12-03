from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.name},{self.description}'
        
# Create a model
# python3 manage.py makemigrations
# python3 migrate
# import into templates > admin.py
#  views > make a DogCreate for crud functions

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.name},{self.description}'