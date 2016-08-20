# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from .models import Station, Event
from django.contrib.auth.decorators import login_required
from .forms import EventForm, StationForm


def post_page(request, station_id):
    user = request.user if request.user.is_authenticated() else None
    try:
        if user:
            station = Station.objects.get(id=station_id)
        else:
            station = Station.objects.get(id=station_id, visible=True)
    except Station.DoesNotExist:
        raise Http404(u"网页不存在")
    if user:
        events = station.event_set.all()
    else:
        events = station.event_set.all().filter(visible=True)
    content = {
        'user': user,
        'station': station,
        'events': events,
    }
    return render(request, 'post.html', content)


@login_required
def event_add(request, station_id):
    user = request.user if request.user.is_authenticated() else None
    if not user:
        raise ConnectionRefusedError
    try:
        station = Station.objects.get(id=station_id)
    except Station.DoesNotExist:
        raise Http404(u"网页不存在")
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.station = station
            event.save()
            return HttpResponseRedirect(reverse('post_page', args=(station.pk,)))
        else:
            content = {
                'form': form,
                'station': station
            }
            return render(request, 'manage/event_add.html', content)
    else:
        form = EventForm()
        content = {
            'form': form,
            'station': station
        }
        return render(request, 'manage/event_add.html', content)


@login_required
def event_edit(request, event_id):
    user = request.user if request.user.is_authenticated() else None
    if not user:
        raise ConnectionRefusedError
    try:
        event = Event.objects.get(id=event_id)
    except Station.DoesNotExist:
        raise Http404(u"网页不存在")
    station = event.station
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post_page', args=(station.pk,)))
        else:
            content = {
                'form': form,
                'station': station
            }
            return render(request, 'manage/event_edit.html', content)
    else:
        form = EventForm(instance=event)
        content = {
            'form': form,
            'station': station
        }
        return render(request, 'manage/event_edit.html', content)


@login_required
def station_add(request):
    user = request.user if request.user.is_authenticated() else None
    if not user:
        raise ConnectionRefusedError
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            station = form.save(commit=True)
            return HttpResponseRedirect(reverse('post_page', args=(station.pk,)))
        else:
            content = {
                'form': form,
            }
            return render(request, 'manage/station_add.html', content)
    else:
        form = StationForm()
        content = {
            'form': form,
        }
        return render(request, 'manage/station_add.html', content)


@login_required
def station_edit(request, station_id):
    user = request.user if request.user.is_authenticated() else None
    if not user:
        raise ConnectionRefusedError
    try:
        station = Station.objects.get(id=station_id)
    except Station.DoesNotExist:
        raise Http404(u"网页不存在")
    if request.method == 'POST':
        form = StationForm(request.POST, instance=station)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post_page', args=(station.pk,)))
        else:
            content = {
                'form': form,
                'station': station
            }
            return render(request, 'manage/station_edit.html', content)
    else:
        form = StationForm(instance=station)
        content = {
            'form': form,
            'station': station
        }
        return render(request, 'manage/station_edit.html', content)
