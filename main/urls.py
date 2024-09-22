from django.urls import path
from .views import NewsListAPIView, BooksListAPIView, PostsListView


urlpatterns = [
    path('api/v1/news/', NewsListAPIView.as_view()),
    path('api/v1/news/<int:pk>', NewsListAPIView.as_view()),

    path('api/v1/books/', BooksListAPIView.as_view()),
    path('api/v1/books/<int:pk>', BooksListAPIView.as_view()),
    
    path('api/v1/posts/', PostsListView.as_view()),
    path('api/v1/posts/<int:pk>', PostsListView.as_view())
]
