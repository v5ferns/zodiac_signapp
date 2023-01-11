from django.urls import path
from .views import calculate_zodiac_sign, cal_zod

urlpatterns = [
    path("/", calculate_zodiac_sign, name='home'),
    path('form2/', cal_zod),
]