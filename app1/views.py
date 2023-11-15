from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def prasanna1(request):
    return render(request,'prasanna1.html')

def prasu1(request):
    return HttpResponse('hi prasu1')