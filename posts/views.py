from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Post
from django.core import serializers

# Create your views here.

def home_view(request):
    qs = Post.objects.all()
    context = {
        "qs": qs,
        "info": "created for django template",
    }
    return render(request, 'posts/main.html', context)

def post_view_json(request):
    qs = Post.objects.all()
    data = serializers.serialize("json",qs)
    context = {
        "data": data,
    }
    return JsonResponse(context)