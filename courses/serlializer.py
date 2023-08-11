from rest_framework import serializers
from .models import Course

class CourseSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'open_subscription')
