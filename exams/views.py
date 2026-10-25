from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView,CreateAPIView

from exams.models import Assessment
from accounts.models import User
from exams.serializers import AssessmentSerializer
from exams.permissions import OwnerOnly

from datetime import datetime,time,timedelta

class AssessmentListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # def get(self,request):

    #     instance = Assessment.objects.filter(created_by=request.user)

    #     serializer_instance = AssessmentSerializer(instance,many=True)

    #     return Response(data=serializer_instance.data)

    serializer_class = AssessmentSerializer
    queryset = Assessment.objects.all()

class AssessmentCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    serializer_class = AssessmentSerializer

    def perform_create(self, serializer):

        serializer.save(created_by=self.request.user)

    # def post(self,request):

    #     form_data = request.data

    #     serializer_instance = AssessmentSerializer(data=form_data)

    #     if serializer_instance.is_valid():

    #         serializer_instance.save(created_by=request.user)

            # cleaned_data = serializer_instance.validated_data    

            # exam_date = cleaned_data.get("exam_date")
            # start_time = cleaned_data.get("start_time")
            # duration = cleaned_data.get("duration")

            # exam_end_datetime = (datetime.combine(exam_date,start_time)+timedelta(hours=duration))

            # end_time = exam_end_datetime.time()

            # existing_assessments = Assessment.objects.filter(exam_date=exam_date)

            # for assessments in existing_assessments:

            #     existing_start = assessments.start_time
            #     exisiting_end = assessments.end_time

            #     if start_time<exisiting_end and end_time>existing_start:

            #         raise ValidationError({"assessment_time":"there is already an assessment on the entered time"})

            # cleaned_data["end_time"] = end_time

            # instance = Assessment.objects.create(**cleaned_data,created_by=request.user)

            # serializer_instance = AssessmentSerializer(instance)

        #     return Response(data=serializer_instance.data)

        # else:

        #     return Response(data=serializer_instance.errors)

class AssessmentRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [OwnerOnly]

    def get(self,request,pk=None):

        instance = get_object_or_404(Assessment,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instance = AssessmentSerializer(instance)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):

        form_data = request.data

        instance = get_object_or_404(Assessment,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instance = AssessmentSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Assessment,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response({"message":"deleted"})

    