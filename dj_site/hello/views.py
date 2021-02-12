from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.


# https://www.youtube.com/watch?v=Ye8mB6VsUHw

def sessfun(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4: del (request.session['num_visits'])
    resp = HttpResponse('view count=' + str(num_visits))
    resp.set_cookie('dj4e_cookie', '3284b792', max_age=1000)
    return resp
