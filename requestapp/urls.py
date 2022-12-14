from django.urls import path
from requestapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('request/', views.RequestList.as_view()),
    path('request/<int:pk>/', views.request_detail),

    path('talimger-request/', views.RequestTypeTwoList.as_view()),
    path('talimger-request/<int:pk>/', views.requestTypeTwo_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)