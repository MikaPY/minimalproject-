from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


def index(request):
    print(request)
    return HttpResponse("Hello World!")


def test(request):
    return HttpResponse('<h1> Test Page </h1>')


def show(request):
    res = Pizza.objects.all()
    context = {'res': res}
    return render(request, 'show.html', context)
