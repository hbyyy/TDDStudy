from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Item


def home_page(request):
    # TODO: support more the one list

    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('item_text'))
        return redirect('home')
    return render(request, 'lists/home.html', context={'items': Item.objects.all()})
