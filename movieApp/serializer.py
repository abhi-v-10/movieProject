from rest_framework import serializers
from movieApp.models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"
    def validate_imdb_rating(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("IMDB rating must be between 0 and 10.")
        return value
    def validate_runtime(self, value):
        if value <= 0:
            raise serializers.ValidationError("Runtime must be a positive integer.")
        return value
    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError("Movie name is required.")
        if not data.get('language'):
            raise serializers.ValidationError("Language is required.")
        if not data.get('rel_year'):
            raise serializers.ValidationError("Release year is required.")
        if not data.get('genre'):
            raise serializers.ValidationError("Genre is required.")
        if not data.get('hero'):
            raise serializers.ValidationError("Hero name is required.")
        if not data.get('heroine'):
            raise serializers.ValidationError("Heroine name is required.")
        return data
        