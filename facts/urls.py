from django.urls import path
from .views import *


urlpatterns = [
    path('fact/<int:amount>/', FactListView.as_view(), name='Fact-list'),
    path('fact/create/', FactCreateView.as_view(), name='fact-create'),
]