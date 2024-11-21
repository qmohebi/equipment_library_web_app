from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import Category, Location, EquipmentModel, LoanLocation


class LoanRequest(forms.Form):
    selected_model = forms.ModelMultipleChoiceField(
        queryset=EquipmentModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        error_messages={"required": "Please select a model from below!"},
        # to_field_name="equip_model_id",
    )

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
        label="Location",
        empty_label="Select a location",
        required=True,
        queryset=LoanLocation.objects.all(),
    )

    requester_name = forms.CharField(
        label="Enter your name",
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "e.g. John"}),
    )
    extension = forms.IntegerField(
        label="Extension",
        required=True,
        widget=forms.NumberInput(attrs={"placeholder": "Enter your extension number"}),
    )
    # notes = forms.Textarea()
    notes = forms.CharField(
        label="Additional notes",
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter additional information like patient MRN",
                "inputmode": "numeric",
            }
        ),
        # required=False caused submit spinner and modal to not function properly. So made note required
    )

    def create_loan(self, model, requester_name, extension) -> dict:
        """create a loan on the db and sent the loan request 
        and model as dict"""
        pass

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = "id-ModelSelectionForm"
    #     self.helper.form_class = "form-group"
    #     self.helper.form_method = "post"
    #     self.helper.form_action = "success/"
    #     self.helper.layout = Layout(
    #         Row(
    #             "location",
    #             Column("requester_name", css_class="form-group col-md-6 mb-0"),
    #             Column("extension", css_class="form-group col-md-6 mb-0"),
    #             "notes",
    #         )
    #     )

    #     # self.helper.form_tag = True

    #     self.helper.add_input(
    #         Submit(
    #             "submit",
    #             "Submit",
    #             css_class="btn submit-btn rounded px-5",
    #             **{"data-bs-toggle": "modal", "data-bs-target": "#staticBackdrop"}
    #         )
    #     )


class LogisticsRequestForm(forms.Form):
    equipment_number = forms.CharField(
        label="equipment number",
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "e.g. 5512345"}),
    )
    request_details = forms.CharField(
        label="Enter your name",
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "e.g. John"}),
    )
    planned_date = forms.DateField(
        label="planned-date",
        required=True,
        widget=forms.TextInput(attrs={"type": "date"}),
    )

    def create_request(self):
        print("form_succesfully_submitted")
