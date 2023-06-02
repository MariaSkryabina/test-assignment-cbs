from django.shortcuts import render


def index(request):
    main_data = {
        'title':'Главная cтраница'
    }
    return render(request, 'main/index.html', main_data)


def login(request):
    return render(request, 'main/login.html')
# Create your views here.
