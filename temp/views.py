# from django.shortcuts import render


from meuapp.models import Pessoa
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import PessoaSerializer


def hello_world(request):
    return HttpResponse('Hello world')


class PessoaView(ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class PessoaListView(ListAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class PessoaDetailView(RetrieveAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class PessoaCreateView(CreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class PessoaUpdateView(UpdateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


pessoaboa = PessoaView.as_view()
pessoa = PessoaListView.as_view()
pessoa_detail = PessoaDetailView.as_view()
pessoa_insert = PessoaCreateView.as_view()
pessoa_update = PessoaUpdateView.as_view()