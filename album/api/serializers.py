from rest_framework import serializers
from app.models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('title', 'photo', 'photo_webp', 'created_at')