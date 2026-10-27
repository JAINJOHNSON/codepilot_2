

from django.urls import path

from problem.views import QuestionCreateView


urlpatterns = [

    # route to token authentication
    path("assessment/<int:pk>/question/",QuestionCreateView.as_view()),  

]