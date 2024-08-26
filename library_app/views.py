
from .forms import CategorySelectionForm
from django.views.generic import FormView
from django.urls import reverse_lazy

# from django.shortcuts import render

# def home(request):
#     return render(request, 'library+a')


class HomePageView(FormView):
    # model = Category
    template_name = "home.html"
    form_class = CategorySelectionForm
    success_url= reverse_lazy("")

    def form_valid(self, form):
        selected_categories = form.cleaned_data["selected_categories"]
        selected_location = form.cleaned_data["location"]

        return super.form_valid(form)

