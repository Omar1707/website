from django.http import Http404
from django.http import HttpResponse
from django.template import Context,loader

def index(request):
    template = loader.get_template("homepage/index.html")
    return HttpResponse(template.render())