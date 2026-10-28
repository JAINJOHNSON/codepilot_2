
from rest_framework import serializers

from datetime import datetime

from exams.models import Assessment
from problem.models import Question

from django.db.models import Sum

from problem.serializer import QuestionSerializer

class AssessmentSerializer(serializers.ModelSerializer):

    greetings = serializers.SerializerMethodField(read_only=True)    # to call field not in model serializermethodfield is used
    question_count = serializers.SerializerMethodField(read_only=True)
    total_score = serializers.SerializerMethodField(read_only=True)
    questions = serializers.SerializerMethodField(read_only=True)



    created_by = serializers.StringRelatedField()

    class Meta:

        model = Assessment

        fields = "__all__"

        read_only_fields = ["id","end_time","created_by"]

    def validate(self,validated_data):

        exam_date = validated_data.get("exam_date")

        if exam_date<datetime.today().date():

            raise serializers.ValidationError("Please enter a valid exam_date")

        return validated_data

    def get_greetings(self,obj):

        return "good morning"

    def get_question_count(self,obj):
        return Question.objects.filter(assessment=obj).count()

    def get_total_score(self,obj):
        return Question.objects.filter(assessment=obj).values("score").aggregate(total=Sum("score")).get("total")

    def get_questions(self,obj):
        question_objects = Question.objects.filter(assessment=obj)
        serializer_instance = QuestionSerializer(question_objects,many=True)
        return serializer_instance.data

    
    


        