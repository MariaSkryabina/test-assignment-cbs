from django.shortcuts import render


def events_home(request):
    main_data = {
        'title': 'Мероприятия'
    }
    return render(request, 'events/events.html', main_data)
