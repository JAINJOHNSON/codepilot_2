from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework import serializers

from evaluation.permissions import isStudentUser
from evaluation.models import Submission,Answer
from evaluation.serializers import SubmissionSerializers,AnswerSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication


from exams.models import Assessment

from problem.models import Question


class SubmisstionStartView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [isStudentUser]

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,isStudentUser]

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


"""  will work
class AnswerUpdateView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def patch(self,request,pk=None):
        answer_id = pk
        form_data = request.data

        answer_obj = get_object_or_404(Answer, id=answer_id)
        serializer_instance = AnswerSerializer(data=form_data,instance=answer_obj,partial=True)

        if serializer_instance.is_valid():
            # serializer_instance.save()
            # return Response(data=serializer_instance.data)
            Answer.objects.filter(id=answer_id).update(**form_data)
            response_data = {"message":"answer evaluated"}
            return Response(data=response_data)

        else:
            return Response(data=serializer_instance.errors)

"""
# another method

class AnswerUpdateView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]



    def patch(self,request,pk=None):
        answer_id = pk
        form_data = request.data

        #check awarded_marks is more than question_max mark 
        given_score = form_data.get("marks_awarded")    #added
        print("marks_awarded = ",given_score)           #added

        
        
        

        #    till here



        answer_obj = get_object_or_404(Answer, id=answer_id)
        serializer_instance = AnswerSerializer(data=form_data,instance=answer_obj,partial=True)

        serializer_instance.fields["marks_awarded"].read_only=False
        serializer_instance.fields["feedback"].read_only=False

        #
        question_id = answer_obj.question.id
        print("Question ID:", question_id)

        question_score = answer_obj.question.marks
        print("maximum marks",question_score)


        if serializer_instance.is_valid():
            print(serializer_instance.validated_data)
            serializer_instance.save()
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)