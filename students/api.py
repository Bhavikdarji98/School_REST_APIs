from django.http.response import JsonResponse
from students import serializers
from rest_framework.views import APIView
from rest_framework import viewsets
import students
from students.models import Student, Teacher, Lecture
from students.serializers import LectureSerializer, StudentSerializer, TeacherSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from functools import partial, reduce
from django.db.models import Q, manager


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    List all workers, or create a new worker.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class LectureViewSet(viewsets.ModelViewSet):
    """
    List all workkers, or create a new worker.
    """
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    ordering_fields = ['time']