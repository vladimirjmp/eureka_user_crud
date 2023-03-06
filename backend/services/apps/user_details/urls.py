# Django
from django.urls import path

# Libraries
from user_details import views

urlpatterns = [
    path("", views.CreateUserView.as_view(), name="create-user"),
    path("/<int:id>", views.GetUserView.as_view(), name="create-user"),
]
