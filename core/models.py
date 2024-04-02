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
    


class Dessert(models.Model):
    name=models.CharField("Desert name ",max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    dessert_image=models.ImageField(upload_to="desert_image",blank=True,null=True)
    decription = models.TextField("Desert Description")

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.username

class OrderedItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    dessert = models.ForeignKey(Dessert,on_delete=models.CASCADE)
    quantity = models.IntegerField()     

    def totalPrice(self):
        return self.dessert.price * int(self.quantity)

    
    
