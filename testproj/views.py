__author__ = 'systryonka'

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
import  datetime

def current_datetime(request):
    time = datetime.datetime.now()
    html = "TIME: %s" % time
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    html = "OFFSET= %s" % offset
    return HttpResponse(html)

