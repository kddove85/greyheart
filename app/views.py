from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Greyhound
from .models import BoardMember


def index(request):
    greys_list = Greyhound.objects.all().filter(is_spotlight=True)
    context = {'greys_list': greys_list}
    return render(request, 'app/index.html', context)


def about_us(request):
    board_members_list = BoardMember.objects.all()
    context = {'board_members_list': board_members_list}
    return render(request, 'app/about_us.html', context)


def available_greys(request):
    available_greys_list = Greyhound.objects.all().filter(is_available=True)
    context = {'available_greys_list': available_greys_list}
    return render(request, 'app/available_greys.html', context)


def adopt(request):
    pass
