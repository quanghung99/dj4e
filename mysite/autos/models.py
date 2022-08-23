from operator import mod
from pyexpat import model
from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Make(models.Model):
    name: models.CharField(
        max_length=200,
        help_text='Enter a make (e.g. Mercedes)',
        validators=[MinLengthValidator(2,'Make must be greater than 1 character')]
    )


    def __str__(self):
        """strings for representing the Model object"""
        return self.name
    
class Auto(models.Model):
    nickname: models.CharField(
        max_length=200,
        help_text='''Enter a auto's name''',
        validators=[MinLengthValidator(2,'Nickname must be greater than 1 character')]
    )
    milage: models.PositiveIntegerField()
    comments: models.CharField(max_length=200)
    make: models.ForeignKey('Make', on_delete=models.CASCADE, null=False)

    # shows up in the admin list
    def __str__(self):
        return self.nickname
    