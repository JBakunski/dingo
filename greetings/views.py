from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Hello World!")


def greeting(request, name):
    return HttpResponse(f"Hello {name.title()}!")

