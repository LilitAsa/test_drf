from django.forms.models import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Category


class PostApiView(APIView):
    def get(self, request):
        posts = Post.objects.values()
        return Response({"posts": list(posts)})
    
    def post(self, request):
        title = request.data.get("title")
        content = request.data.get("content")
        category_id = request.data.get("category")
        category = Category.objects.get(id=category_id)
        new_post = Post.objects.create(title=title, content=content, category=category)
        return Response({"post": model_to_dict(new_post)})
    
    
    
    def put(self, request):
        id = request.data.get("id")
        title = request.data.get("title")
        content = request.data.get("content")
        category_id = request.data.get("category")
        category = Category.objects.get(id=category_id)
        Post.objects.filter(id=id).update(title=title, content=content, category=category)
        return Response({"post": model_to_dict(Post.objects.get(id=id))})
    
    def delete(self, request):
        id = request.data.get("id")
        Post.objects.filter(id=id).delete()
        return Response({"status": "success"})  
    

class PostDetailApiView(APIView):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        return Response({"post": post})
    
    def put(self, request, id):
        title = request.data.get("title")
        content = request.data.get("content")
        category_id = request.data.get("category")
        category = Category.objects.get(id=category_id)
        Post.objects.filter(id=id).update(title=title, content=content, category=category)
        return Response({"post": model_to_dict(Post.objects.get(id=id))})
    
    def delete(self, request, id):
        Post.objects.filter(id=id).delete()
        return Response({"status": "success"})
    
    
    



