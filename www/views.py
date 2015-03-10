import datetime
import calendar

from django.shortcuts import render
from django.conf import settings

from www.models import Event, Registrant


def home(request):
    cd = {}
    return render(request, 'www/home.html', cd)

def cal(request, year=None, month=None):
    cd = {}
    now = datetime.datetime.now()
    
    if not year:
        year = now.year
    if not month:
        month = now.month
    
    year = int(year)
    month = int(month)
    if month < 12:
        next_month_number = month + 1
    else:
        next_month_number = 1
    next_month_name = settings.CAL_MONTHS.get(next_month_number, 'Unknown Next?')
    if month > 1:
        prev_month_number = month - 1
    else:
        prev_month_number = 12
    
    events = Event.objects.filter(from_time__year=year, from_time__month=month)
    cd['events'] = {}
    for event in events:
        events_list = cd['events'].get(event.from_time.day, [])
        events_list.append(event)
        cd['events'][event.from_time.day] = events_list
    
    c = calendar.Calendar(calendar.SUNDAY)
    cd['cal'] = c.monthdays2calendar(year, month)
    cd['month_name'] = settings.CAL_MONTHS.get(month, 'Unknown?')
    cd['month_number'] = month
    cd['year'] = year
    cd['next_month_number'] = next_month_number
    cd['next_month_name'] = next_month_name
    
    return render(request, 'www/cal.html', cd)

