from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import New, Book, Post

# Create your views here.



class NewsListAPIView(APIView):
    def get(self, request):

        news = New.objects.all()

        news_list = []

        for n in news:
            news_list.append({"title": n.title, "description": n.description, "created_at": n.created_at})
        
        return Response(news_list)
    

class BooksListAPIView(APIView):
    def get(self, request):

        books = Book.objects.all()

        books_list = []

        for b in books:
            books_list.append({"title": b.title, "description": b.description, "author": b.author, "pages_count": b.pages_count})
        
        return Response(books_list)
    

class PostsListView(APIView):
    def get(self, request):

        posts = Post.objects.all()

        posts_list = []

        for p in posts:
            posts_list.append({"title": p.title, "description": p.description, "created_at": p.created_at})

        return Response(posts_list)
