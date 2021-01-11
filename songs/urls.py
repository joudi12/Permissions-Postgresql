from django.contrib import admin
from django.urls import path, include


from .views import SongsListView, SongDetailsView


urlpatterns = [
    path('', SongsListView.as_view(), name='songs'),
    path('<int:pk>/', SongDetailsView.as_view(), name='songs_details'),
]