from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from task1.models import Student
from task1.serializers import StudentSerializer
from rest_framework.decorators import action
# Create your views here.

class StudentViewSet(ViewSet):
    
    # get all student info
    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    
    # post student info
    def create(self,request):
        serializer  = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def active_student(self,request,pk=None):
        students = Student.objects.filter(status=True)
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    
class StudentDetailsViewSet(ViewSet):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return None
    
    # get single data
    def retrieve(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    # update student data
    def update(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
    # partial update
    def partial_update(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    
    # delete student data
    def destroy(self, request,pk=None):
        student = self.get_object(pk)
        student.delete()

        return Response({'massage':'student Data delete successfully'})
    
    @action(detail=True, methods=['get','post'])
    def active(self,request,pk=None):
        student = self.get_object(pk)
        student.status=True
        student.save()


        return Response({
            "message": "Student activated successfully",
            "id": student.id,
            "status": student.status
        })
    
    @action(detail=True, methods=['get','post'])
    def deactive(self,request,pk):
        student = self.get_object(pk)
        student.status=False
        student.save()

        return Response({"message": "Student deactivated"})
    
    