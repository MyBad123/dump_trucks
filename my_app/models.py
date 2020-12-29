from django.db import models

class DataRegister(models.Model):
    userInn = models.IntegerField(primary_key=True)
    userOrganizationForm = models.CharField(max_length=40)
    userName = models.CharField(max_length=40)
    userMail = models.EmailField()
    userTel = models.IntegerField()
    userKind = models.CharField(max_length=40)

class LoginPassword(models.Model):
    login = models.ForeignKey('DataRegister', on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    
class RegisterObject(models.Model):
    objectId = models.CharField(max_length=10, primary_key=True)
    objectAdress = models.CharField(max_length=200)
    objectNumber = models.CharField(max_length=200)
    objectV = models.IntegerField()
    objectOplata = models.CharField(max_length=20)
    objectDocuments = models.CharField(max_length=20)
    objectUser = models.ForeignKey('DataRegister', on_delete=models.CASCADE)

class Order(models.Model):
    orderDate = models.DateField()
    orderChange = models.CharField(max_length=20, default='')
    orderV = models.IntegerField(default=1)
    orderPrice = models.IntegerField(default=1)
    orderObject = models.ForeignKey('RegisterObject', on_delete=models.CASCADE)

class Truck(models.Model):
    truckModel = models.CharField(max_length=50)
    truckNumber = models.IntegerField()
    truckSeriesTS = models.IntegerField()
    truckSeriesPT = models.IntegerField()
    truckV = models.IntegerField()
    truckUser = models.ForeignKey('DataRegister', on_delete=models.CASCADE)







