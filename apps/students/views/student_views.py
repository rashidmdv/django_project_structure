from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.permissions.role_permission import IsTeacher



from apps.students.models import Student
from apps.students.serializers import StudentSerializer
from apps.students.services import (
    list_students,
    create_student,
    get_student,
    update_student,
    deactivate_student,
)


class StudentListCreateView(generics.GenericAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsTeacher]
    queryset = Student.objects.all()

    def get(self, request):
        students = list_students(Student)
        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = create_student(serializer.validated_data)
        return Response(self.get_serializer(student).data, status=status.HTTP_201_CREATED)


class StudentDetailView(generics.GenericAPIView):
    serializer_class = StudentSerializer

    def get_object(self, pk):
        return get_student(pk)

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = self.get_serializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = update_student(student, serializer.validated_data)
        return Response(self.get_serializer(student).data)

    def delete(self, request, pk):
        student = self.get_object(pk)
        deactivate_student(student)
        return Response(status=status.HTTP_204_NO_CONTENT)
