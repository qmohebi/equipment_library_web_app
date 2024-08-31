from .forms import ModelSelectionForm, LoanRequestInfo
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .models import Location
from django.shortcuts import render

# from django.shortcuts import render

# def home(request):
#     return render(request, 'library+a')


class HomePageView(FormView):
    # model = Category
    template_name = "home.html"
    form_class = LoanRequestInfo
    success_url = reverse_lazy("library_app:successful_loan")

    def get(self, request, *args, **kwargs):
      loan_form = LoanRequestInfo()
      model_form = ModelSelectionForm()
      return render(request, self.template_name, {"loan_form":loan_form, "model_form":model_form})

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

          return self.form_valid(loan_form)
        else:
            return render(request, self.template_name, {
            "loan_form": loan_form,
            "model_form": model_form
        })


    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)


class SuccessPageView(TemplateView):
    template_name = "successful_loan.html"
