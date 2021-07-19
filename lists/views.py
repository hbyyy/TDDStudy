from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Item, List


def home_page(request):
    return render(request, 'lists/home.html')


def list_view(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', context={'items': items})


def new_list_view(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(reverse('list_view'))
