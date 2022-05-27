from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello World")


def posts(request):
    return HttpResponse('This is a Blog page')


def post_detail(request):
    return HttpResponse('This is a post page')
