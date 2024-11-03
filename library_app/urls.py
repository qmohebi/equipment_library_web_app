from django.urls import path
from .views import (
    HomePageView,
    SuccessPageView,
    OutOfHourPageView,
    LogisticsRequestForm,
)
from datetime import datetime, date
from django.contrib.auth import views as auth_views

app_name = "library_app"

closing_time = "22:30:00"
opening_time = "9:00:00"

now = datetime.now()


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("success/", SuccessPageView.as_view(), name="successful_loan"),
    path("out_of_hour", OutOfHourPageView.as_view(), name="out_of_hour"),
    path("library_logistics", LogisticsRequestForm.as_view(), name="library_logistics"),
    path("accounts/login/", auth_views.LoginView.as_view()),
]
