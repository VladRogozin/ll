from django.urls import path
from .views import WordListView, WordCreateView


urlpatterns = [
    path('word/<str:level>/<int:amount>/', WordListView.as_view(), name='word-list'),
    path('word/create/', WordCreateView.as_view(), name='word-create'),
]