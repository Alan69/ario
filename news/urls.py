from django.urls import path
from news import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('post/<int:pk>/', views.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)