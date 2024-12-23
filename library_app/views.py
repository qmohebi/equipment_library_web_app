from .forms import LoanRequest
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .forms import LogisticsRequestForm
# from django.contrib.auth.mixins import LoginRequiredMixin


import random

from datetime import datetime, time

# from django.shortcuts import render

# def home(request):
#     return render(request, 'library+a')


class HomePageView(FormView):
    # model = Category
    template_name = "home.html"
    form_class = LoanRequest
    # success_url = reverse_lazy("library_app:successful_loan")

    opening_time = time(8, 45)
    closing_time = time(23, 45)

    def out_of_hour(self):
        """
        check if the current date is outside working hours
        and the day is weekend and return true"""
        now = datetime.now()
        current_time = now.time()
        current_day = now.isoweekday()
        return (
            current_day in [6, 7]
            or current_time < self.opening_time
            or current_time > self.closing_time
        )

    def get(self, request, *args, **kwargs):

        # if self.out_of_hour():
        #     return redirect("library_app:out_of_hour")

        loan_form = LoanRequest()
        return render(
            request,
            self.template_name,
            {"loan_form": loan_form},
        )

    # @method_decorator(csrf_exempt)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        loan_form = LoanRequest(request.POST)

        if loan_form.is_valid():
            selected_models = loan_form.cleaned_data.get("selected_model")
            selected_location = loan_form.cleaned_data.get("location")
            name = loan_form.cleaned_data.get("requester_name")
            ext = loan_form.cleaned_data.get("extension")
            notes = loan_form.cleaned_data.get("notes")

            # Example: Generate request numbers for each selected model
            loan_data = []
            for model in selected_models:
                print(model)
                request_number = random.randint(100, 500)
                # request_number = f"{model.pk}-{name[:3].upper()}"  # Generate request number
                loan_data.append(
                    {
                        "request_number": request_number,  # Example: request number
                        "model_name": model.display_name,  # Use a model field that is serializable
                        # Include the primary key if needed
                    }
                )

            # Return JSON response
            return JsonResponse(
                {
                    "status": "success",
                    "loan_data": loan_data,
                }
            )

        return JsonResponse(
            {
                "status": "error",
                "errors": loan_form.errors,
            }
        )

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)


class SuccessPageView(TemplateView):
    template_name = "successful_loan.html"


class OutOfHourPageView(TemplateView):
    template_name = "out_of_hour.html"


class LogisticsRequestForm(FormView):
    template_name = "library_logistics.html"
    form_class = LogisticsRequestForm
    success_url = "./"
    login_url = "./success"

    def form_valid(self, form):
        form.create_request()
        return super().form_valid(form)
