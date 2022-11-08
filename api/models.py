from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)     

class User(models.Model):
    username = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    times_purchased = models.IntegerField(default=0)
    owned_by = models.ForeignKey(User, on_delete=models.PROTECT)

class Payment(models.Model):
    amount = models.FloatField()
    user = models.OneToOneField(User, on_delete=models.PROTECT)

