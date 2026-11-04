
from django.urls import path

from accounts.views import AdminCreateView,StudentCreateView
from accounts.views import ProfileUpdateView,StudentProfileGetView

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [

    # route to admin register view
    path("admin/register/",AdminCreateView.as_view()),

    # route to student register view
    path("student/register/",StudentCreateView.as_view()),

    path("jwt/token/register/",TokenObtainPairView.as_view()),
    path("jwt/token/refresh/",TokenRefreshView.as_view()),

    path("profile/complete/",ProfileUpdateView.as_view()),    # to complete student profile
    path("profile/get/me/",StudentProfileGetView.as_view()),  # to get whole profile view
]