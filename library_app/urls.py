from django.urls import path
from .views import HomePageView

app_name = "library_app"

urlpatterns = [path("", HomePageView.as_view(), name="home")]
