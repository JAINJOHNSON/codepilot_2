from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

from evaluation.permissions import isStudentUser
from evaluation.models import Submission
from evaluation.serializers import SubmissionSerializers

from exams.models import Assessment


class SubmisstionStartView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [isStudentUser]

    def post(self,request,pk=None):
        assessment_id = pk
        
        assessment_object = get_object_or_404(Assessment,id = assessment_id)   # get_bject_or_404   is used so that server not crash when error occurs
        instance = Submission.objects.create(assessment=assessment_object,student=request.user)

        serializer_instance = SubmissionSerializers(instance)
        return Response(data=serializer_instance.data)

