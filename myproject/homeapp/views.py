from django.shortcuts import render

def index(request):
    return render(request,"index.html")


def sec(request):
    return render(request,"sec.html")    


def third(request):
    return render(request,"third.html")    