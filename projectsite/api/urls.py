from django.urls import path
from . import views

urlpatterns = [
    path('colleges/', views.CollegeListCreateAPIView.as_view(), name='college-list-create'),
    path('colleges/<int:pk>/', views.CollegeRetrieveUpdateDestroyAPIView.as_view(), name='college-detail'),
    # Program endpoints
    path('programs/', views.ProgramListCreateAPIView.as_view(), name='program-list-create'),
    path('programs/<int:pk>/', views.ProgramRetrieveUpdateDestroyAPIView.as_view(), name='program-detail'),
    # Student endpoints
    path('students/', views.StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),
]