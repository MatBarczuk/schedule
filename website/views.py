from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


def welcome(request):
    meetings = Meeting.objects.all()
    return render(request, 'website/welcome.html', {'meetings': meetings})
