from django.urls import path

from .views import DataRegisterView

urlpatterns = [
    path('my_data/', DataRegisterView.as_view()),
]

