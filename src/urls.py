from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('api/guess_game/', include('guess_game.urls')),
    path('api/supervisor/', include('supervisor.urls')),
    path('api/facts/', include('facts.urls')),
    path('api/news/', include('news.urls')),
    path('api/dialogs/', include('dialogs.urls')),
    path('api/quotes/', include('quotes.urls')),
    path('api/spells/', include('spells.urls')),
    path('admin/', admin.site.urls),
]
