from django.db import models

class DataRegister(models.Model):
    organization = models.CharField(max_length=40)
    inn = models.IntegerField(primary_key=True)
    allName = models.CharField(max_length=40)
    mail = models.EmailField()
    tel = models.IntegerField()
    userKind = models.CharField(max_length=40)

class LoginPassword(models.Model):
    login = models.ForeignKey('m_DataRegister', on_delete=models.CASCADE)
    password = models.CharField(max_length=20)

class RegisterObject(models.Model):
    adress = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    v = models.IntegerField()
    oplata = models.CharField(max_length=20)
    documents = models.CharField(max_length=20)
    this_user = models.ForeignKey('m_DataRegister', on_delete=models.CASCADE)

class Order(models.Model):
    date = models.DateField()
    nober = models.IntegerField()
    v = models.IntegerField()
    price = models.IntegerField()
    active = models.CharField(max_length=10)
    this_object = models.ForeignKey('m_RegisterObject', on_delete=models.CASCADE)
    this_driver = models.ForeignKey('m_RegisterObject', on_delete=models.CASCADE, null=True)

class Truk(models.Model):
    model_truk = models.CharField(max_length=200)
    numder_truk = models.IntegerField(primary_key = True)
    series_registration = models.CharField(max_length=100)
    series_pts = models.CharField(max_length=100)
    v = models.IntegerField()
    this_driver = models.ForeignKey('m_DataRegister', on_delete=models.CASCADE)

class YesOrder(models.Model):
    v = models.IntegerField()
    truk = models.ForeignKey('m_truk', on_delete=models.CASCADE)
    


    




