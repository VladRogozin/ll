from django.urls import path
from .views import *


urlpatterns = [
    path('go/<int:amount>/', random_data_view, name='spell-list'),
]