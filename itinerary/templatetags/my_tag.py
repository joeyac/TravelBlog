# coding=utf-8
from itinerary.models import *
from django import template


def public_station_list():
    return Station.objects.filter(visible=True).order_by('-arrival_time')


def event_belong_to_station(station_id):
    try:
        station = Station.objects.get(id=station_id)
    except:
        raise KeyError
    return station.event_set.all().filter(visible=True)

register = template.Library()
register.assignment_tag(public_station_list, name="public_station_list")
register.assignment_tag(event_belong_to_station, name="event_belong_to_station")
