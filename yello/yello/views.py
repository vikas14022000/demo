from django.shortcuts import render
import numpy
import pandas
def home(request):
    return render(request,"base.html")