from django.urls import path

from .views import (DataRegisterView, LoginPasswordView,
                    UsersObjectView, RegisterObjectOneView, 
                    RegisterObjectView, OrderView,
                    TruckView)

urlpatterns = [
    path('main/', DataRegisterView.as_view()),
    path('user/', LoginPasswordView.as_view()),
    path('userobject/', UsersObjectView.as_view()),
    path('registeroneobject/', RegisterObjectOneView.as_view()),
    path('registerobject/', RegisterObjectView.as_view()),
    path('order/', OrderView.as_view()),
    path('trucks/', TruckView.as_view())
]
