from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello to my first page~")
def add(request):
    return HttpResponse("Add..")