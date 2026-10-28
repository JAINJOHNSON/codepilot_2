from django.shortcuts import render

# Create your views here.



from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView


from exams.models import Assessment

from problem.serializer import QuestionSerializer

from problem.models import Question




class QuestionCreateView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,pk = None):
        assessment_id = pk
        assessment_object = Assessment.objects.get(id = assessment_id)

        form_data = request.data

        serializer_instance = QuestionSerializer(data = form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(assessment=assessment_object,created_by=request.user)

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


class QuestionsRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    