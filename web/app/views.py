from django.shortcuts import render
from django.http import HttpResponse
from app.models import Stu
# Create your views here.
def index(request):
    return HttpResponse("Hello to my first page~")
def add(request):
    lists = Stu.objects.all()
    for stu in lists:
        print(stu)
    print(Stu.objects.get(id=2))
    return HttpResponse("Add..")
def produce(request):
    return HttpResponse("produce..")