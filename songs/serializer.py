from rest_framework import serializers

from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'lyrics', 'title', 'publisher')
        model = Song