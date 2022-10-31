from django.urls import path

from comic.views import comicAPI

urlpatterns = [
    path('comic/<int:pk>', comicAPI),
]
# http://127.0.0.1:8000/cleint/
