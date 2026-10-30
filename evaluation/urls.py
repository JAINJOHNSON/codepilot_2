

from django.urls import path

from evaluation.views import SubmisstionStartView,SubmissionRetriveApiView,AnswerCreateView
from evaluation.views import AnswerUpdateView



urlpatterns = [
                path("assessment/<int:pk>/submission/",SubmisstionStartView.as_view()),             # check    
                path("submission/<int:pk>",SubmissionRetriveApiView.as_view()),
                path('submission/<int:pk>/answer/',AnswerCreateView.as_view()),
                path('answer/<int:pk>/',AnswerUpdateView.as_view()),
]