
from django.urls import path

from accounts.views import AdminCreateView,StudentCreateView

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [

    # route to admin register view
    path("admin/register/",AdminCreateView.as_view()),

    # route to student register view
    path("student/register/",StudentCreateView.as_view()),

    path("jwt/token/register/",TokenObtainPairView.as_view()),
    path("jwt/token/refresh/",TokenRefreshView.as_view())
]