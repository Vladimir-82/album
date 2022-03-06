from rest_framework import serializers
from app.models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('title', 'photo', 'created_at')