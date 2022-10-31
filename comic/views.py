from .models import Comic
from .serializers import ComicSer
from rest_framework import generics


class ComicView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Comic.objects.all()
    serializer_class = ComicSer
    lookup_field = 'pk'


comicAPI = ComicView.as_view()
