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
        serializer.save()
        return Response({"post": serializer.data})
    
    def put(self, request,*args,**kwargs):
        pk = kwargs.get("pk", None)
        print(kwargs.get("pk"))
        if not pk:
            return Response({"error": "Method Put is not allowed"})
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({"error": "Object not found"})
        serializer = PostSerializer(instance=instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    
    def delete(self, request,*args,**kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Delete is not allowed"})
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({"error": "Object not found"})
        instance.delete()
        return Response({"post": f"{str(instance.title)} is deleted"})
    

    


