
from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken
from exams.views import AssessmentListView,AssessmentCreateView,AssessmentRetrieveUpdateDeleteView

urlpatterns = [

    # route to token authentication
    path("assessment/token/",ObtainAuthToken.as_view()),   

    # route to assessment list view
    path("assessment/all/",AssessmentListView.as_view()),

    # route to assessment create view
    path("assessment/add/",AssessmentCreateView.as_view()),

    # route to assessment retrieve,update,delete view
    path("assessment/<int:pk>/",AssessmentRetrieveUpdateDeleteView.as_view()),
]