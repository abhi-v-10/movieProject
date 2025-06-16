from rest_framework import serializers
from movieApp.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# class DetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MovieDetails
#         exclude = ['id']

#         def validate_budget(self, value):
#             if value < 0:
#                 raise serializers.ValidationError("Budget cannot be negative.")
#             return value
#         def validate_collection(self, value):
#             if value < 0:
#                 raise serializers.ValidationError("Collection cannot be negative.")
#             return value

#         def validate(self, data):
#             if not data.get('budget'):
#                 raise serializers.ValidationError("Budget is required.")
#             if not data.get('collection'):
#                 raise serializers.ValidationError("Collection is required.")
#             return data

# class ProductionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Production
#         exclude = ['id']

#     def validate_name(self, value):
#         if not value:
#             raise serializers.ValidationError("Production name is required.")
#         return value

# class OtherLanguagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OtherLanguages
#         exclude = ['id']

#     def validate_other_language(self, value):
#         if not value:
#             raise serializers.ValidationError("Other language is required.")
#         return value


class MovieSerializer(serializers.ModelSerializer):

    # details = DetailsSerializer(required=False)
    # production = ProductionSerializer(required=False)
    # other_languages = OtherLanguagesSerializer(many=True, required=False)

    class Meta:
        model = Movies
        exclude = ['id']

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'mobilenumber', 'age']
    
    def validate_mobilenumber(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Mobile number must contain only digits.")
        if len(value) < 10 or len(value) > 15:
            raise serializers.ValidationError("Mobile number must be between 10 and 15 digits.")
        return value
    
    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        return value    
        

class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['password'] = user.password
        token['age'] = user.age
        return token
    

