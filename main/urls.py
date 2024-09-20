from django.urls import path
from .views import NewsListAPIView, BooksListAPIView, PostsListView


urlpatterns = [
    path('api/v1/news', NewsListAPIView.as_view()),
    path('api/v1/books', BooksListAPIView.as_view()),
    path('api/v1/posts', PostsListView.as_view())
]
