from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_dajngo(request):
    return render (request,'course/courseinfo.html')