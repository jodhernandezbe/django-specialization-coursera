from django.http import HttpResponse
from django.template import loader

def myview(request):
    template = loader.get_template('hello/hello.html')
    response = HttpResponse(template.render({'text': '85ca5257'}, request))
    response.set_cookie('dj4e_cookie', '85ca5257', max_age=1000)
    return response