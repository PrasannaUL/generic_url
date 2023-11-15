from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def prasanna3(request):
    return render(request,'prasanna3.html')

def prasu3(request):
    return HttpResponse('hi prasu3')