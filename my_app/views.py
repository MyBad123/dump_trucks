import random
import string
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *
from .my_scripts import *

#for time
import datetime

#for dataRegister
class DataRegisterView(APIView):
    def get(self, request):
        reg = m_DataRegister.objects.all()
        ser = DataRegisterSerializer(reg, many = True)
        return Response({"registers": ser.data})

    def post(self, request):
        new_user = request.data.get("new_user")

        inn = str(new_user.inn)


        my_str = ''
        if len(inn) == 12 or len(inn) == 10:
            new_user.all_name = my_inn(inn)
            my_str = ''
            for hz in range(10):
                 my_str += random.choice(string.ascii_letters)
            my_mail(str(new_user.inn), my_str)
        else:
            Return("no")

            
        ser = DataRegisterSerializer(data = new_user)
        if ser.is_valid(raise_exception = True):
            ser.save()

        b = m_LoginPassword()
        b.login = int(new_user.inn)
        b.password = my_str

        b.save()

        return Response("yes")


class LoginPasswordView(APIView):
    #чтоб зайти 
    def post(self, request):
        stat = str(request.data.get('status'))
            
        if stat == 'old':
            my_login = str(request.data.get('login'))
            my_pass = str(request.data.get('password'))
            
            b = m_LoginPassword.objects.get(login = my_login)
            if b.password == my_pass:
                bb = m_DataRegister.objects.get(inn = int(requesq.data.get('inn'))) 
                ser = DataRegisterSerializer(data = bb)

                return Response({"about_user": ser.data})
        
        if stat == 'new':
            old_login = str(request.data.get('old_login'))
            b = m_LoginPassword.objects.get(login = old_login)
            b.login = str(request.data.get('new_login'))
            b.password = str(request.data.get('new_password'))
            b.save()
            return Response("yes")
        
        return Response("no")

class RegisterObjectView(APIView):
    def post(self, request):
        stat = str(request.data.get('status'))
        if stat == 'new':
            b = m_RegisterObject()
            #create new
            b.adress = str(request.data.get('adress'))
            b.number = str(request.data.get('number'))
            b.v = int(request.data.get('v'))
            b.oplata = str(request.data.get('oplata'))
            b.documents = str(request.data.get('documents'))
            b.this_user = int(request.data.get('this_user'))
            
            b.save()
            return Response({"status": "create new object"})

        if stat == 'old':
            my_objects = m_RegisterObject.objects.get(this_user = int(request.data.get('this_user')))
            my_serializer = RegisterObjectSerializer(my_objects, many = True)

            return Response({"objects": my_serializer.data})

        if stat == 'object':
            my_object = m_RegisterObject.objects.get(pk = int(request.data.get('id')))
            my_serializer = RegisterObjectSerializer(data=my_object)
            
            return Response({"object": my_serializer.data})

class OrderView(APIView):
    def post(self, request):
        stat = str(request.data.get('status'))
        
        if stat == 'new':
            work_with_date = str(request.data.get('date'))
            my_date = datetime.date(int(work_with_date[6] + work_with_date[7] + work_with_date[8] + work_with_date[9]), int(work_with_date[3] + work_with_date[4]), int(work_with_date[0] + work_with_date[1]))

            #in now day?
            if m_Order.objects.get(date = my_date):
                b = m_Order.objects.get(date = my_data)

                if m_Order.objects.get(date = my_date) and b.this_object == int(request.data.get('this_object')):
                    return Response("no")

            #create new order
            b = m_Order()
            b.date = my_date
            b.nober = int(request.data.get('noder'))
            b.v = int(request.data.get('v'))
            b.price = int(request.data.get('price'))
            b.active = str(request.data.get('active'))
            b.this_object = int(request.data.get('this_object'))
            b.save()

            return Response("yes")

        if stat == 'this_order':
            b = m_Order.objects.get(pk = int(request.data.get('pk')))
            ser = OrderSerializer(data = b)
            
            return Response({"order": ser.data})

    def delete(request):
        b = m_Order(pk = int(request.data.get('pk')))
        
        bb = m_DataRegister.objects.get(b.this_driver)
        b.delete()
        
        mysms(str(bb.tel))
        
        b.delete()

        return Response("yes")
            
            
            
#для перевозчиков 
class truckView(APIView):
    def post(request):
        if str(request.data.get('status')) == 'trucks_of_user':
            user_trucks = m_truk.objects.get(this_driver = int(request.data.get('this_driver')))
            ser = trukSerializer(user_trucks, many = True)

            return Response({"trucks": ser.data})

        if str(request.data.get('status')) == 'truck':
            number = m_truk.objects.get(numder_truk = int(request.data.get('numder_truk')))
            ser = trukSerializer(data = user_trucks)
            
            return Response({"truck": ser.data})

        if str(request.data.get('status')) == 'new_truck':
            if m_truk.objects.get(int(request.data.get('numder_truk'))) or m_truk.objects.get(int(request.data.get('series_registration'))) or m_truk.objects.get(int(request.data.get('series_pts'))):
                return Response("no")
            
            b = m_truk()
        
            b.model_truk = request.data.get('model_truk')
            b.numder_truk = request.data.get('numder_truk')
            b.series_registration = request.data.get('series_registration')
            b.series_pts = request.data.get('series_pts')
            b.v = request.data.get('v')
            b.this_driver = request.data.get('this_driver')            

    def update(request):
        b = m_truk.objects.get(numder_truk = int(requests.data.get('numder_truk')))
        
        b.model_truk = request.data.get('model_truk')
        b.numder_truk = request.data.get('new_numder_truk')
        b.series_registration = request.data.get('series_registration')
        b.series_pts = request.data.get('series_pts')
        b.v = request.data.get('v')
        b.this_driver = request.data.get('this_driver')

        b.save()

    def delete(request):
        b = m_truk.objects.get(numder_truk = int(requests.data.get('numder_truk')))
        b.delete()
                
            
            




            
        


        


