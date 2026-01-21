from django.urls import path
from .views import *

urlpatterns = [
    path('', Register.as_view(), name='Register'),
    path('update/<int:pk>/', UpdateRegister.as_view(), name='UpdateRegister'),
]