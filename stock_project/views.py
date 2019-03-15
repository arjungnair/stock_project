from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html',name)
def about(render):
    return render(request, 'index.html')