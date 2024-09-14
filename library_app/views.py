from .forms import ModelSelectionForm, LoanRequestInfo
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from datetime import datetime, time

# from django.shortcuts import render

# def home(request):
#     return render(request, 'library+a')


class HomePageView(FormView):
    # model = Category
    template_name = "home.html"
    form_class = LoanRequestInfo
    success_url = reverse_lazy("library_app:successful_loan")

    opening_time = time(8,45)
    closing_time = time(23, 45)

    def out_of_hour(self):
        """
        check if the current date is outside working hours
        and the day is weekend"""
        now = datetime.now()
        current_time = now.time()
        current_day = now.isoweekday()
        return current_day in [6, 7] or current_time < self.opening_time or current_time > self.closing_time


    def get(self, request, *args, **kwargs):

        # if self.out_of_hour():
        #     return redirect("library_app:out_of_hour")
        
        loan_form = LoanRequestInfo()
        model_form = ModelSelectionForm()
        return render(
            request,
            self.template_name,
            {"loan_form": loan_form, "model_form": model_form},
        )

    def post(self, request, *args, **kwargs):
        loan_form = LoanRequestInfo(request.POST)
        model_form = ModelSelectionForm(request.POST)

        if loan_form.is_valid() and model_form.is_valid():
            selected_models = model_form.cleaned_data.get("selected_model")
            selected_location = loan_form.cleaned_data.get("location")
            name = loan_form.cleaned_data.get("requester_name")
            ext = loan_form.cleaned_data.get("extension")
            notes = loan_form.cleaned_data.get("notes")

            print(name, ext, notes, selected_location)

            for model_id in selected_models:
                print(model_id)
                # take model id and location id
                # write to the database
                # get a loan request number for each model
                # send to front end

            return self.form_valid(loan_form)
        else:
            return render(
                request,
                self.template_name,
                {"loan_form": loan_form, "model_form": model_form},
            )

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)


class SuccessPageView(TemplateView):
    template_name = "successful_loan.html"


class OutOfHourPageView(TemplateView):
    template_name = 'out_of_hour.html'
