# coding: utf-8
from annoying.decorators import render_to


@render_to('home.html')
def home(request):
    return {}


@render_to('train.html')
def train(request):
    return {}
