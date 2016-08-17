from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import Station, Event


class StationAdmin(SummernoteModelAdmin):
    list_display = ('pk', 'title', 'create_time', 'last_update_time',
                    'arrival_time', 'leave_time', )
    list_display_links = ('pk', 'title',)


class EventAdmin(SummernoteModelAdmin):
    list_display = ('pk', 'title', 'create_time', 'last_update_time',
                    'start_time', 'end_time',
                    )
    list_display_links = ('pk', 'title',)

admin.site.register(Station, StationAdmin)
admin.site.register(Event, EventAdmin)
