import io
from .models import Post
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    category_id = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField()
    image = serializers.ImageField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.image = validated_data.get('image', instance.image)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance
