from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Course
from .serializer import CourseSerializer



class CourseList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
