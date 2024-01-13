from django.urls import path
from .views import *


urlpatterns = [
    path('new/<int:amount>/', NewListView.as_view(), name='new-list'),
    path('new/create/', NewCreateView.as_view(), name='new-create'),
]