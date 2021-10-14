from django.urls import path, include
from rest_framework import routers
from .views import hello_world, pessoa, pessoa_update, pessoa_insert, pessoa_detail, pessoaboa

urlpatterns = [
    path('hello', hello_world, name='hello2'),
    path('pessoaboa', pessoaboa, name='list_pessoa'),
    path('pessoaboa/<int:pk>', pessoaboa, name='list_pessoa'),
    path('pessoa', pessoa, name='list_pessoa'),
]
