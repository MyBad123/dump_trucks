from rest_framework import serializers

from .models import *

class DataRegisterSerializer(serializers.Serializer):
    organization = serializers.CharField(max_length=40)
    inn = serializers.IntegerField()
    all_name = serializers.CharField(max_length=40)
    mail = serializers.EmailField()
    tel = serializers.IntegerField()
    user_kind = serializers.CharField(max_length=40)

    def create(self, valited_data):
        return m_DataRegister.objects.create(**valited_data)

class LoginPasswordSerializer(serializers.Serializer):
    login = serializers.IntegerField()
    password = serializers.CharField(max_length=20)

class RegisterObjectSerializer(serializers.Serializer):
    adress = serializers.CharField(max_length=200)
    number = serializers.CharField(max_length=200)
    v = serializers.IntegerField()
    oplata = serializers.CharField()
    documents = serializers.CharField()
    this_user = serializers.IntegerField()

class OrderSerializer(serializers.Serializer):
    date = serializers.DateField()
    nober = serializers.IntegerField()
    v = serializers.IntegerField()
    price = serializers.IntegerField()
    active = serializers.CharField(max_length=10)
    this_object = serializers.CharField(max_length=100)
    this_driver = serializers.CharField(max_length=100)

class trukSerializer(serializers.Serializer):
    model_truk = serializers.CharField(max_length=200)
    numder_truk = serializers.IntegerField()
    series_registration = serializers.CharField(max_length=100)
    series_pts = serializers.CharField(max_length=100)
    v = serializers.IntegerField()
    this_driver = serializers.CharField(max_length=100)

class YesOrderSerializer(serializers.Serializer):
    v = serializers.IntegerField()
    truk = serializers.CharField(max_length=100)
    