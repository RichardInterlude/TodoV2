from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . serializers import TaskSerializer, CategorySerializers
from . models import Task, Category


from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated



class TaskView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            serializers = TaskSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save(owner=request.user)
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request):
        try:
            task = Task.objects.filter(owner=request.user)
            serializers = TaskSerializer(task, many = True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self, request):
        try:
            task = Task.objects.filter(owner=request.user)
            task.delete()
            return Response({'message':'All Tasks Deleted Successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        try:
            task = get_object_or_404(Task, id=id, owner=request.user)
            serializers = TaskSerializer(task)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, id):
        try:
            task = get_object_or_404(Task, id=id, owner=request.user)
            serializers = TaskSerializer(task, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)