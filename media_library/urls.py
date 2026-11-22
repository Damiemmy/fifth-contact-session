from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("library/", views.library, name="library"),
    path("upload/", views.upload_media, name="upload_media"),
    path("media/<int:pk>/", views.media_detail, name="media_detail"),
]
