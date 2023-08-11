
from rest_framework import viewsets
from .serlializer import CourseSerealizer
from .models import Course

# Create your views here.
class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerealizer
    queryset = Course.objects.all()
