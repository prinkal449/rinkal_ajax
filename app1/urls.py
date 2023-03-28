from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('create_row/', create_row, name='create_row'),
    path('del-row/', del_row, name='del_row')
]