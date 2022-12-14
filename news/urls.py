<<<<<<< HEAD
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

=======
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

>>>>>>> ae24838919602f6967e2b9720be28cac4d9e3380
urlpatterns = format_suffix_patterns(urlpatterns)