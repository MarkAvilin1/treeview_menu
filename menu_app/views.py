from django.shortcuts import render


def index(request, name):
    return render(request, 'index.html', {'name': name})
