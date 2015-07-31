from datetime import datetime
from Calendar.calendar import models
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response


def main(request):
    return render_to_response('main.html')


def events(request):
    events = serializers.serialize("json", models.Event.objects.all(), fields=('date', 'text'))
    return HttpResponse(events)


def add_event(request):
    if request.method == "POST":
        date = request.POST.get('date')
        notification = request.POST.get('notification')
        if not date or not notification:
            return HttpResponse({'error': 'validation error'})

        converted_date = datetime.strptime(date, '%d/%m/%Y').strftime('%Y-%m-%d')
        models.Event.objects.create(date=converted_date, text=notification)
    return HttpResponse('POST')
