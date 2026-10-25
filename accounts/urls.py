
from django.urls import path

from accounts.views import AdminCreateView,StudentCreateView

urlpatterns = [

    # route to admin register view
    path("admin/register/",AdminCreateView.as_view()),

    # route to student register view
    path("student/register/",StudentCreateView.as_view()),
]