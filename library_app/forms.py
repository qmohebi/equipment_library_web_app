from django import forms
from .models import Category, Location


class CategorySelectionForm(forms.Form):
    selected_categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    location = forms.ModelChoiceField(
        queryset=Location.objects.all(), empty_label="Select a location", required=True
    )
