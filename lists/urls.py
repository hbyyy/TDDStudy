from django.urls import path

from .views import new_list_view, list_view, add_item_view

urlpatterns = [
    path('new', new_list_view, name='new_list_view'),
    path('<int:list_id>/', list_view, name='list_view'),
    path('<int:list_id>/add_item', add_item_view, name='add_item_view')
]
