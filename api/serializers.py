from .models import Post
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
import io
from rest_framework.parsers import JSONParser


class PostModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        
    def __str__(self):
        return self.title

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()

def encode():
    model = PostModel(
        title="Crypto, Inflation, Bonds: Your Investment Guide to a Risky Year",
        content="This year has already been … a lot. The whole AI narrative that was powering the US stock market is being called into question. There’s little certainty about how a second Donald Trump administration will affect the finances of average Americans, and whether we’ll see inflation rise again."
    )
    model_sr = PostSerializer(model)
    print(model_sr.data, type(model_sr.data), sep="\n")
    json = JSONRenderer().render(model_sr.data)
    print(json)
    return json

def decode():
    json = encode()
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = PostSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
    return serializer.validated_data