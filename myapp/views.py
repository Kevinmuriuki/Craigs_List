from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


# Create your views here.
def home(req):
    return render(req, 'base.html')


def new_search(req):
    search = req.POST.get('search')
    frontend_stuff = {
        'search': search,
    }
    return render(req, 'my_app/new_search.html', frontend_stuff)
