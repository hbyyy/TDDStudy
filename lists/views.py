from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Item, List


def home_page(request):
    return render(request, 'lists/home.html')


def list_view(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'lists/list.html', context={'list': list_})


def new_list_view(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(reverse('list_view', args=[list_.id]))


def add_item_view(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(reverse('list_view', args=[list_.pk]))
