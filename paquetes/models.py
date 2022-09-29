from django.db import models
from django.forms import CharField

class Municipio(models.Model):
    pos_code = models.CharField(max_length=10, primary_key=True,primary_key=True)
    municipio = models.CharField(max_length=20, blank=False)
    

class Address (models.Model):
    id_address = models.CharField(max_length=100, primary_key=True,primary_key=True)
    address = models.CharField(max_length=100, blank=False, null=False )
    neighborhood = models.CharField(max_length=100, blank=False, null=False)
    
class Location(models.Model):
    id_location = models.CharField(max_length=100, blank=False, null=False, primary_key=True)
    departamento = models.OneToOneField(Municipio)
    address = models.ForeignKey(Address)
    
class User(models.Model):
    identify = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
 
class Type (models.Model):
    id_type= models.CharField(max_length=4, blank=False, null=False, primary_key=True) 
    type = models.CharField(max_length=20, blank=False, null=False) 
    
class State(models.Model):
    id_state= models.CharField(max_length=4, blank=False, null=False, primary_key=True) 
    state = models.CharField(max_length=20, blank=False, null=False) 
    date = models.DateField()    
    
class Package(models.Model):
     id_package = models.CharField(max_length=255, blank=False, null=False, primary_key=True)
     type = models.ForeignKey(Type)
     weight = models.IntegerField(null=True, blank=False)
     description = models.TextField(max_length=200,blank=False, null=True)

    
class ShippingOrder(models.Model):
    id_shipping = models.CharField(max_length=255, blank=False, null=False,primary_key=True)
    date = models.DateField(null=False)
    sender = models.ForeignKey(User)
    addressee = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    state = models.ManyToManyField(State)
    package = models.OneToOneField(Package)