from django.http import JsonResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import StudentViewSet, ClientListView, create_or_get_students, StudentDetailView




urlpatterns = [
     path('api/clients/', create_or_get_students, name='client-list'),
     path('api/clients/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
]