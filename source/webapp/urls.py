from django.urls import path
from webapp.views import game_page, stats_page


urlpatterns = [
    path('', game_page),
    path('stats/', stats_page)
]