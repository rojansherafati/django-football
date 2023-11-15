from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
#    path('test/',views.test),
 #   path('test2/',views.test2),
    path('search/',views.search),
    path('players/get/all/',views.players_get_all),
    path('clubs/search/',views.clubs_search)
]