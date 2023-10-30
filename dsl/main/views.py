from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html')


def delivery(request):
    return render(request, 'main/delivery.html')
