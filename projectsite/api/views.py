from rest_framework import generics
from studentorg.models import College, Program, Student 
from .serializers import CollegeSerializer, ProgramSerializer, StudentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# List all or create new colleges (protected)
class CollegeListCreateAPIView(generics.ListCreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]  # Require login or token

# Retrieve, update, or delete a single college (protected)
class CollegeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]  # Require login or token

    # List all programs or create one (protected)
class ProgramListCreateAPIView(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]  # Require token/login

# Retrieve, update, delete a program (protected)
class ProgramRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]

# List all students or create one (protected)
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

# Retrieve, update, delete a student (protected)
class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
