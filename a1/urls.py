from django.urls import path 
from . import views

urlpatterns=[
    path("home",views.home),
    path("lamp1_on",views.lamp1_on),
    path("lamp1_off",views.lamp1_off),
    path("lamp2_on",views.lamp2_on),
    path("lamp2_off",views.lamp2_off),
    path("lamp3_on",views.lamp3_on),
    path("lamp3_off",views.lamp3_off),
    path("lamp4_on",views.lamp4_on),
    path("off_all",views.all_off),
    
]
