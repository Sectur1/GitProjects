from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    if(request.method == "POST"):
        request.FILES
