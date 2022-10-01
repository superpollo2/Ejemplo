from django.db import models

    
class Departamento(models.Model):
    id_departamento = models.CharField(max_length=10, primary_key=True,null=False)
    departament = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return self.id_departamento

class Address (models.Model):
    id_address = models.CharField(max_length=100, primary_key=True)
    address = models.CharField(max_length=100, blank=False, null=False )
    neighborhood = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.id_address
    
class Location(models.Model):
    pos_code = models.CharField(max_length=100, null= False)
    departamento= models.ForeignKey(Departamento,on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete = models.CASCADE)
    municipio = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.pos_code
    
class User(models.Model):
    identify = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    
    
    def __str__(self):
        return self.identify
 
class Type (models.Model):
    id_type= models.CharField(max_length=4, blank=False, null=False, primary_key=True) 
    type = models.CharField(max_length=20, blank=False, null=False) 
    
    def __str__(self):
        return self.id_type
 
class Date(models.Model):
    date = models.DateField(primary_key=True)
    
    def __str__(self):
        return self.date
        
class State(models.Model):
    id_state= models.CharField(max_length=4, blank=False, null=False, primary_key=True) 
    state = models.CharField(max_length=20, blank=False, null=False) 
    date = models.ManyToManyField(Date)
    
    def __str__(self):
        return self.state
    

    
class Package(models.Model):
     id_package = models.CharField(max_length=255, blank=False, null=False, primary_key=True)
     type = models.ForeignKey(Type, on_delete = models.CASCADE)
     weight = models.IntegerField(null=True, blank=False)
     description = models.TextField(max_length=200,blank=False, null=True)
     
     def __str__(self):
        return self.id_package

    
class ShippingOrder(models.Model):
    id_shipping = models.CharField(max_length=255, blank=False, null=False,primary_key=True)
    date = models.ForeignKey(Date, on_delete = models.CASCADE)
    sender = models.ForeignKey(User, on_delete = models.CASCADE,related_name='remitente')
    addressee = models.ForeignKey(User, on_delete = models.CASCADE, related_name='destinatario')
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    state = models.ManyToManyField(State)
    package = models.OneToOneField(Package, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.id_shipping