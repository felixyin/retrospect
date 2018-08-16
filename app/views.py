from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView

from .models import *


# Create your views here.


# 核销详情
class WineItemDetailView(DetailView):
    model = WineItem


def wine_item(request, id):
    wi = get_object_or_404(WineItem, id=id)
    wi.count += 1
    if wi.first_visit_time is None:
        wi.first_visit_time = now()
    wi.last_visit_time = now()
    wi.save()

    banners = HomeAttach.objects.all()

    return render(request, 'app/show.html', {'wi': wi, 'banners': banners})
