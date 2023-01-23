from django.urls import path
from urequest import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('international/', views.RequestList.as_view()),
    path('international/<int:pk>/', views.request_detail),

    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.student_detail),

    path('courses/', views.CoursesList.as_view()),
    path('courses/<int:pk>/', views.courses_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)