import imp
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('familiares/', familiares),        
    path('familiares2/', familiares2),        

]