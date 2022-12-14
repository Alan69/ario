from django.urls import path
from news import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('post/<int:pk>/', views.post_detail),

    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.article_detail),

    path('comment/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.comment_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)