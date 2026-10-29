

from django.urls import path

from evaluation.views import SubmisstionStartView



urlpatterns = [
                path("assessment/<int:pk>/submission/",SubmisstionStartView.as_view()),             # check    
]