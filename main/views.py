from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import New, Book, Post
from .serializers import NewsSerializer, BooksSerializer, PostSerializer
# Create your views here.



class NewsListAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            new = New.objects.get(pk=pk)
            serializer = NewsSerializer(new)
            return Response(serializer.data)
        else:
            news = New.objects.all()
            serializer = NewsSerializer(news, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serialier = NewsSerializer(data=request.data)
        if serialier.is_valid():
            serialier.save()
            return Response(serialier.data)
        return Response(serialier.errors)
    
    def put(self, request, pk):
        new = New.objects.get(pk=pk)
        serializer = NewsSerializer(new, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        new = New.objects.get(pk=pk)
        new.delete()
        return Response({"detail": "O'chirildi!"})

    

class BooksListAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            book = Book.objects.get(pk=pk)
            serializer = BooksSerializer(book)
            return Response(serializer.data)
        else:
            books = Book.objects.all()
            serializer = BooksSerializer(books, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response({"detail": "O'chirildi!"})


class PostsListView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        else:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = BooksSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response({"detail": "O'chirildi!"})
