from rest_framework import serializers
from .models import (DataRegister, RegisterObject,
                    Order, Truck)

class DataRegisterSerializer(serializers.ModelSerializer):
    """ user's data"""

    class Meta:
        model = DataRegister
        fields = ('userInn', 'userOrganizationForm', 
                'userName', 'userMail',
                'userTel', 'userKind')


class LoginPasswordSerializer(serializers.Serializer):
    login = serializers.IntegerField()
    password = serializers.CharField(max_length=20)


class RegisterObjectSerializer(serializers.ModelSerializer):
    """it is data of user's objects"""

    class Meta:
        model = RegisterObject
        exclude = ("objectUser",)

class OrderSerializer(serializers.ModelSerializer):
    """for order"""

    date = serializers.CharField(max_length=20)
    class Meta:
        model = Order
        exclute = ("orderDate", "orderObject", )

class TruckSerializer(serializers.ModelSerializer):
    """fiels of trucks"""

    class Meta:
        model = Truck
        exclute = ("truckUser")











