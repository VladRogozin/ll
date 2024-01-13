from django.urls import path
from .views import *


urlpatterns = [
    path('quote/<int:amount>/', QuoteListView.as_view(), name='quote-list'),
    path('quote/create/', QuoteCreateView.as_view(), name='quote-create'),
]