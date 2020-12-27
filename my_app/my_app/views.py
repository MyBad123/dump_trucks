import random
import string
import requests
import urllib
import smtplib
import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serialisers import (DataRegisterSerializer, LoginPasswordSerializer, 
                        RegisterObjectSerializer)
from .models import (DataRegister, LoginPassword, 
                    RegisterObject, Order)
from django.core.exceptions import ObjectDoesNotExist
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class DataRegisterView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    def post(self, request):
        newINN: str = str(request.data.get("inn"))
        userTel = str(request.data.get("tel"))
        userMail = str(request.data.get("userMail"))
        userOrganizationForm = str(request.data.get("organizationForm"))
        userKind = str(request.data.get("kind"))
        userPass: str = ''
        userName: str
        #for all name
        if len(newINN) == 10:
            checkInnResult = requests.get('https://api-fns.ru/api/egr?req=' + newINN + '&key=14f39eb135e66a0884789dda6939865d40190880')
            jsonINN = json.loads(checkInnResult.text)
            userName = str(jsonINN["items"][0]["ЮЛ"]["НаимСокрЮЛ"])
        elif len(newINN) == 12:
            checkInnResult = requests.get('https://api-fns.ru/api/egr?req=' + newINN + '&key=')
            jsonINN = json.loads(checkInnResult.text)  
            userName = str(jsonINN["items"][0]["ИП"]["ФИОПолн"])
        else:
            return Response("no", status=status.HTTP_400_BAD_REQUEST)
        #for new password
        for times in range(10):
            userPass += random.choice(string.ascii_letters)
        #new password in your email
        mailMsg = MIMEMultipart()
        mailTo = userMail
        mailMessage = 'login: ' + newINN + ' password: ' + userPass
        mailMsg.attach(MIMEText(mailMessage, 'plain'))
        mailServer = smtplib.SMTP('smtp.mail.ru: 25')
        mailServer.starttls()
        mailServer.login('gena.kuznetsov@internet.ru', 'o%pdUaeIUI12')
        mailServer.sendmail('gena.kuznetsov@internet.ru', mailTo, mailMsg.as_string())
        mailServer.quit()
        #save data
        newData = DataRegister()
        newData.userInn = newINN
        newData.userOrganizationForm = userOrganizationForm
        newData.userName = userName
        newData.userMail = userMail
        newData.userTel = userTel
        newData.userKind = userKind
        newData.save()
        #save login and password 
        newAccount = LoginPassword()
        newAccount.login = newINN
        newAccount.password = userPass
        newAccount.save()
        return Response(status=status.HTTP_201_CREATED)

class DataRegisterOneView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    def post(self, request):
        try:
            thisUser = DataRegister.objects.get(userInn=str(request.data.get("inn")))
            serializer = DataRegisterSerializer(data=thisUser)
            return Response({serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class LoginPasswordView(APIView):
    def get(self, requst):
        return Response("it is get", status=status.HTTP_200_OK)
    def post(self, request):
        userLogin = int(request.data.get('login'))
        userPassword = int(request.data.get('password'))
        try:
           LoginPassword.objects.get(login=userLogin, password=userPassword)
           return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND)
    def update(self, request):
        userLogin = int(request.data.get('login'))
        userPassword = int(request.data.get('password'))
        try:
            newUserData = DataRegister.objects.get(userInn=userLogin)
            newUserLoginPass = LoginPassword.objects.get(login=userLogin, password=userPassword)
            newUserLoginPass.login = int(request.data.get('new_login'))
            newUserLoginPass.password = str(request.data.get('new_password'))
            newUserLoginPass.save()
            return Response(status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND)

##########################################################################

class UsersObjectView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    def post(self, request):
        thisUser = int(request.data.get("user"))
        try:
            usersObjects = RegisterObject.objects.filter(objectUser=thisUser)
            serializer = RegisterObjectSerializer(usersObjects, many=True)
            return Response({"objects": serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist: 
            return Response(status=status.HTTP_404_NOT_FOUND)


class RegisterObjectView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    def post(self, request):
        newObject = RegisterObject()
        id: str = ''
        forWhile: int = 0
        while forWhile == 0:
            for times in range(10):
                id += random.choice(string.ascii_letters)
            try:
                RegisterObject.objects.get(objectId=id)
            except ObjectDoesNotExist:
                forWhile += 1
        newObject.objectId = id
        newObject.objectAdress = str(request.data.get('adress'))
        newObject.objectNumber = str(request.data.get('number'))
        newObject.objectV = int(request.data.get('v'))
        newObject.objectOplata = str(request.data.get('oplata'))
        newObject.objectDocuments = str(request.data.get('document'))
        newObject.objectUser = DataRegister.objects.get(userInn=int(request.data.get('user')))
        newObject.save()
        return Response(status=status.HTTP_201_CREATED)
    def put(self, request):
        id = str(request.data.get("id"))
        updateObject = RegisterObject.objects.get(objectId=id)
        updateObject.objectAdress = str(request.data.get('adress'))
        updateObject.objectNumber = str(request.data.get('number'))
        updateObject.objectV = int(request.data.get('v'))
        updateObject.objectOplata = str(request.data.get('oplata'))
        updateObject.objectDocuments = str(request.data.get('document'))
        updateObject.objectUser = DataRegister.objects.get(userInn=int(request.data.get('user')))
        updateObject.save()
        return Response(status=status.HTTP_200_OK)

class RegisterObjectOneView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    def post(self, request):
        id = str(request.data.get("id"))
        thisObject = RegisterObject.objects.get(objectId=id)
        serializer = RegisterObjectSerializer()

        serializer.objectId = thisObject.objectId
        serializer.objectAdress = thisObject.objectAdress
        serializer.objectNumber = thisObject.objectNumber
        serializer.objectV = thisObject.objectV
        serializer.objectOplata = thisObject.objectOplata
        serializer.objectDocuments = thisObject.objectDocuments
        
        return Response({serializer.data}, status=status.HTTP_200_OK)


class OrderView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    def post(self, request):
        newOrder = Order()
        newOrder.orderDate = str(request.data.get('date'))
        newOrder.orderChange = int(request.data.get('change'))
        newOrder.orderPrice = int(request.data.get('price'))
        newOrder.orderV = int(request.data.get('v'))
        newOrder.save()
        return Response(status=status.HTTP_201_CREATED)
    def delete(self, request):
        
        






        
        
        
        
        





