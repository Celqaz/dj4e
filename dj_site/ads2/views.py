from django.shortcuts import render
from .owner import *
from .models import Ad


# Create your views here.
class AdListView(OwnerListView):
    model = Ad
    template_name = 'ads/index.html'


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price','text']


class AdDeleteView(OwnerDeleteView):
    model = Ad
