from django.urls import path
from .views import HomePageView, SuccessPageView

app_name = "library_app"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("success/", SuccessPageView.as_view(), name="successful_loan"),
]
