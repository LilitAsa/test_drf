import io
from .models import Post
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.forms.models import model_to_dict


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    category_id = serializers.IntegerField()  
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    slug = serializers.SlugField(read_only=True)    
    
    
    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.category_id = validated_data.get('category_id', instance.category_id)
    #     instance.save()
    #     return instance
