from django.urls import path
from .views import HomePageView, SuccessPageView, OutOfHourPageView
from datetime import datetime, date

app_name = "library_app"

closing_time = "20:30:00"
opening_time = "9:00:00"

now = datetime.now()

# if date.isoweekday(now) == 6 or date.isoweekday(now) == 7:
#     urlpatterns = [
#         path("", OutOfHourPageView.as_view(), name="out_of_hour"),
#     ]
# elif now.strftime("%H:%M:%S") > closing_time or now.strftime("%H:%M:%S") < opening_time:
#     urlpatterns = [
#         path("", OutOfHourPageView.as_view(), name="out_of_hour"),
#     ]
# else:
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("success/", SuccessPageView.as_view(), name="successful_loan"),
]
