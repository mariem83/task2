from .models import Comic
from rest_framework import serializers


class ComicSer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = '__all__'
