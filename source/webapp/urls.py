from django.urls import path
from webapp.views import game_page


urlpatterns = [
    path('', game_page)
]