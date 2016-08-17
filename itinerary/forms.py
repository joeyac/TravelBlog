# -*- coding: utf-8 -*-
from django import forms
from datetimewidget.widgets import DateTimeWidget
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Event, Station


class StationForm(forms.ModelForm):
    class Meta:
        widgets = {
            'arrival_time': DateTimeWidget(usel10n=True, bootstrap_version=3,
                                           attrs={'width': '100%'}),

            'leave_time': DateTimeWidget(usel10n=True, bootstrap_version=3,
                                         attrs={'width': '100%'}),
            'intro': SummernoteWidget(attrs={'width': '100%'})
        }
        labels = {

        }
        model = Station
        fields = '__all__'

        exclude = ['create_time', 'last_update_time']


class EventForm(forms.ModelForm):
    class Meta:
        widgets = {
            'start_time': DateTimeWidget(usel10n=True, bootstrap_version=3,
                                         attrs={'width': '50%'}),

            'end_time': DateTimeWidget(usel10n=True, bootstrap_version=3,
                                       attrs={'width': '50%'}),

            'description': SummernoteWidget()
        }
        labels = {

        }
        model = Event
        fields = '__all__'

        exclude = ['create_time', 'last_update_time', 'station']
