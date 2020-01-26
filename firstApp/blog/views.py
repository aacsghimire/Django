from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hello Blog</h1>')


def about(request):
    return HttpResponse('<h2>ABOUT</h2>')
