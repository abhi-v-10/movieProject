from rest_framework import serializers
from movieApp.models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"