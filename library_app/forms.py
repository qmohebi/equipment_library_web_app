from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import Category, Location, EquipmentModel, LoanLocation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Row, Column, Layout


class LoanRequestInfo(forms.Form):
    exclude_location = [
        "45B7DCD1518B4F289BF692BD28EE8F45",
        "45EE813FF5D442AFB799B48F49C50C75",
        "614353F632C442B1A1F4F353965CA129",
        "619FB2C31CB64F298C4AA4C17C4EF8B9",
        "8D008371-0C50-4F4C-9918-C4C185725DA2",
        "STG2005081100002",
        "951CB87BFBF347039BCD60D4C31785BA",
        "",
    ]
    location = forms.ModelChoiceField(
        label="Select location from dropdown",
        empty_label="Select a location from the dropdown",
        queryset=LoanLocation.objects.all(),
    )

    requester_name = forms.CharField(
        label="Enter your name",
        max_length=200,
        required=True,
    )
    extension = forms.IntegerField(
        label="Your Extension",
        required=True,
    )
    # notes = forms.Textarea()
    notes = forms.CharField(
        label="Additional notes",
        max_length=200,
        widget=forms.Textarea(attrs={"placeholder": "Enter additional information like patient MRN"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-ModelSelectionForm"
        self.helper.form_class = "form-group"
        self.helper.form_method = "post"
        self.helper.form_action = "success/"
        self.helper.layout = Layout(
            Row(
                "location",
                Column("requester_name", css_class="form-group col-md-6 mb-0"),
                Column("extension", css_class="form-group col-md-6 mb-0"),
                "notes",
            )
        )

        # self.helper.form_tag = True

        self.helper.add_input(Submit("submit", "Submit"))


class ModelSelectionForm(forms.Form):
    selected_model = forms.ModelMultipleChoiceField(
        queryset=EquipmentModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        error_messages={"required": "Please select a model from below!"},
        # to_field_name="equip_model_id",
    )