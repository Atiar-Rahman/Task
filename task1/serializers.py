from rest_framework.serializers import ModelSerializer
from task1.models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['created_at','updated_at','status',]
