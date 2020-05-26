from rest_framework import serializers

from .models import Art, Artist, Period

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'nationality', 'image')

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('id', 'name')

class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = ('id', 'name', 'created', 'image', 'location', 'artist', 'period', 'user')
 
class PopulateArtSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    period = PeriodSerializer(many=True)

    class Meta:
        model = Art
        fields = ('id', 'name', 'created', 'image', 'location', 'artist', 'period', 'user')
 
    def validate_image(self, value):
      if not value.startswith('http'):
        raise serializers.ValidationError({'image': 'Image must start with http'})
      return value