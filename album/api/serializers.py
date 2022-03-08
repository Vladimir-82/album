from rest_framework import serializers
from app.models import App


class AppGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('author', 'title', 'photo_webp', 'created_at')


class AppPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('author', 'title', 'photo', 'created_at')
