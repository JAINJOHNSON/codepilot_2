from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework import serializers

from evaluation.permissions import isStudentUser
from evaluation.models import Submission
from evaluation.serializers import SubmissionSerializers,AnswerSerializer


from exams.models import Assessment

from problem.models import Question


class SubmisstionStartView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [isStudentUser]

    def post(self,request,pk=None):
        assessment_id = pk
        
        assessment_object = get_object_or_404(Assessment,id = assessment_id)   # get_bject_or_404   is used so that server not crash when error occurs
        instance = Submission.objects.create(assessment=assessment_object,student=request.user)

        serializer_instance = SubmissionSerializers(instance)
        return Response(data=serializer_instance.data)

class SubmissionRetriveApiView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [isStudentUser]

    def get(self,request,pk=None):
        submission_id = pk
        instance = get_object_or_404(Submission,id = submission_id )
        serializer_instance = SubmissionSerializers(instance)
        return Response(data=serializer_instance.data)

            

        


class AnswerCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[isStudentUser]

    def post(self,request,pk=None):

        submission_id = pk
        submission_obj=get_object_or_404(Submission,id=submission_id)
        form_data=request.data

        #validaion start
        assessment_object = submission_obj.assessment
        assessment_question = Question.objects.filter(assessment=assessment_object).values_list("id",flat=True)
        question = form_data.get("question")
        # print (question)
        # print(assessment_question)

        if question not in assessment_question:
            raise serializers.ValidationError("invalid Question, Question does not exist")

        #validation over



        serializer_inst=AnswerSerializer(data=form_data)
        if serializer_inst.is_valid():

            serializer_inst.save(submission=submission_obj)

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)