from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    class Optional(models.TextChoices):
        DBMS='DB','DBMS'
        NETWORKING='NET','networking'

    name = models.CharField(max_length=20)
    major = models.CharField(max_length=20)
    optional=models.CharField(max_length=50,choices=Optional.choices)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    emp_name = models.CharField("name",max_length=50)

    def __str__(self):
        return f"Employee Name :{self.emp_name}"

 
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Pastry(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pastry = models.ForeignKey(Pastry, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    def total_price(self):
        return self.pastry.price * self.quantity

    def __str__(self):
        return f'user: {self.user} quantity :{self.quantity}'
    