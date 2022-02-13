from django.urls import path
from .views import *
urlpatterns=[
    path('remove_inventory/',RemoveInventory.as_view()),
    path('add_inventory/<str:type>/',AddInventory.as_view()),
]