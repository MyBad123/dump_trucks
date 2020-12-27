from rest_framework import serializers

class DataRegisterSerializer(serializers.Serializer):
    userInn = serializers.IntegerField()
    organizationForm = serializers.CharField(max_length=40)
    userName = serializers.CharField(max_length=40)
    userMail = serializers.EmailField()
    userTel = serializers.IntegerField()
    userKind = serializers.CharField(max_length=40)

class LoginPasswordSerializer(serializers.Serializer):
    login = serializers.IntegerField()
    password = serializers.CharField(max_length=20)


class RegisterObjectSerializer(serializers.Serializer):
    objectId = serializers.CharField(max_length=10)
    objectAdress = serializers.CharField(max_length=200)
    objectNumber = serializers.CharField(max_length=200)
    objectV = serializers.IntegerField()
    objectOplata = serializers.CharField(max_length=20)
    objectDocuments = serializers.CharField(max_length=20)









