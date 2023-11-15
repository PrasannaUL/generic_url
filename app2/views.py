from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def prasanna2(request):
    return render(request,'prasanna2.html')

def prasu2(request):
    return HttpResponse('hi prasu2')