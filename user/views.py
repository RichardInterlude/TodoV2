from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import login, logout, authenticate
from . serializers import *
from . models import *
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated




class RegisterView(APIView):
    def post(self, request):
        try:
            serializers = RegisterSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self,request,id):
        try:
            register = get_object_or_404(Profile, id=id)
            serializers = RegisterSerializer(register,data=request.data, partial=True) 
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
    def post(self,request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return Response ({'message':'User Login Successfully'},status=status.HTTP_200_OK)
            return Response ({'message':'Invalid username or password'},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LogoutView(APIView):
    def post(self,request):
        permission_classes = [IsAuthenticated]
        try:
            logout(request)
            return Response({'message':'User Logout Successfully'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request):
        try:
            user = request.user
            user.delete()
            return Response({'message':'User Deleted Successfully'},status=status.HTTP_200_OK) 
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)