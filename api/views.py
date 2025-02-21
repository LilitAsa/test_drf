from django.forms.models import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Category
from .serializers import PostSerializer
from django.forms.models import model_to_dict



class PostApiView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response({
                "posts": PostSerializer(posts, many=True).data
            }
        )
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_post = Post.objects.create(
            title=request.data.get("title"),
            content=request.data.get("content"),
            category_id=request.data.get("category_id"),
        )
        serializer.save()
        return Response({"post": model_to_dict(new_post)})
    
    def put(self, request):
        slug = request.data.get("slug")
        if Post.objects.filter(slug=slug).exists():
            return Response({"error": "Slug already exists"}, status=400)
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


    


