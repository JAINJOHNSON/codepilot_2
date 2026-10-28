

from django.urls import path

from problem.views import QuestionCreateView
from problem.views import QuestionsRetriveUpdateDeleteView

urlpatterns = [

    # route to token authentication
    path("assessment/<int:pk>/question/",QuestionCreateView.as_view()),
    path("question/<int:pk>/",QuestionsRetriveUpdateDeleteView.as_view()),


]