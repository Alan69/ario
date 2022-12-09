from django.urls import path
from requestapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('request/', views.RequestList.as_view()),
    path('request/<int:pk>/', views.request_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)