from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import User,StudentProfile
from accounts.serializers import UserSerializer,StudentProfileSerializer

class AdminCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_superuser(role="admin",**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class StudentCreateView(APIView):

    def post(self,request):
        form_data = request.data
        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data
            instance = User.objects.create_user(**cleaned_data)
            serializer_instance = UserSerializer(instance)
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import authentication,permissions

from evaluation.permissions import isStudentUser

class ProfileUpdateView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,isStudentUser]
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def put(self,request):
        form_data = request.data
        student_profile_object = StudentProfile.objects.get(student=request.user)
        serializer_instance = StudentProfileSerializer(data=form_data,instance=student_profile_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

from evaluation.permissions import isStudentUser


class StudentProfileGetView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,isStudentUser]

    def get(self,request):

        instance = request.user.student

        serializer_instance = StudentProfileSerializer(instance)

        return Response(data=serializer_instance.data)

