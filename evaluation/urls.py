

from django.urls import path

from evaluation.views import SubmisstionStartView,SubmissionRetriveApiView,AnswerCreateView



urlpatterns = [
                path("assessment/<int:pk>/submission/",SubmisstionStartView.as_view()),             # check    
                path("submission/<int:pk>",SubmissionRetriveApiView.as_view()),
                path('submission/<int:pk>/answer/',AnswerCreateView.as_view()),
]