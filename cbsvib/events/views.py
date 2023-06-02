from django.shortcuts import render
from .models import Events


def events_home(request):
    events = Events.objects.all()
    return render(request, 'events/events.html', {"events":events})


