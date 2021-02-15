from django.shortcuts import render
from .owner import *
# Create your views here.
class AdListView(OwnerListView):
    pass

class AdDetailView(OwnerDetailView):
    pass

class AdCreateView(OwnerCreateView):
    pass


class AdUpdateView(OwnerUpdateView):
    pass

class AdDeleteView(OwnerDeleteView):
    pass
