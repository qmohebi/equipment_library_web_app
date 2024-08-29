from .forms import ModelSelectionForm
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .models import Location

# from django.shortcuts import render

# def home(request):
#     return render(request, 'library+a')


class HomePageView(FormView):
    # model = Category
    template_name = "home.html"
    form_class = ModelSelectionForm
    success_url = reverse_lazy("library_app:successful_loan")

    def form_valid(self, form):

        print(self.request.POST)

        selected_models = form.cleaned_data.get("selected_model")
        selected_location = form.cleaned_data.get("location")
        name = form.cleaned_data.get("requester_name")
        ext = form.cleaned_data.get("extension")
        notes = form.cleaned_data.get("notes")

        # print(ext)
        print(name)
        print(ext)
        print(notes)

        # get the location id for given location name selected
        # location_id = Location.objects.using("equip").filter(
        #     locationshortname=selected_location
        # ).values_list('locationid', flat=True).first()
        # print(f"location_id: {location_id}")

        print(selected_location)


        for model_id in selected_models:
            print(model_id)

        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)


class SuccessPageView(TemplateView):
    template_name = "successful_loan.html"
