from rest_framework import serializers
from .models import Post
from apps.category.serializers import CategorySerializer

class PostSerializers(serializers.ModelSerializer):
    thumbnail = serializers.CharField(source='get_thumbnail')
    video = serializers.CharField(source='get_video')
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'thumbnail',
            'video',
            'description',
            'excerpt',
            'category',
            'published',
            'status'
        ]
