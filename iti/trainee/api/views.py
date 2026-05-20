from .serializers import StudentSerializer
from trainee.models import Trainee
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class StudentViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Trainee.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            trainee = Trainee.objects.get(pk=pk)
        except Trainee.DoesNotExist:
            return Response({"message": "Student not found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(trainee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            trainee = Trainee.objects.get(pk=pk)
        except Trainee.DoesNotExist:
            return Response({"message": "Student not found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(trainee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            trainee = Trainee.objects.get(pk=pk)
        except Trainee.DoesNotExist:
            return Response({"message": "Student not found!"}, status=status.HTTP_404_NOT_FOUND)
        trainee.delete()
        return Response({"message": "Student deleted successfully!"}, status=status.HTTP_200_OK)
