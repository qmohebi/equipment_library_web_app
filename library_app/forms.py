from django import forms
from .models import Category, Location, EquipmentModel


# class CategorySelectionForm(forms.Form):
#     selected_categories = forms.ModelMultipleChoiceField(
#         queryset=Category.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False,
#     )


class ModelSelectionForm(forms.Form):
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
    selected_model = forms.ModelMultipleChoiceField(
        queryset=EquipmentModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        # to_field_name="equip_model_id",
    )
    location = forms.ModelChoiceField(
        queryset=Location.objects.using("equip")
        .filter(
            siteid="STG200404040007",
            inactive=0,
        )
        .exclude(locationtypeid__in=exclude_location)
        .exclude(locationtypeid__isnull=True)
        .order_by("locationshortname"),
        empty_label="Select a location",
        required=True,
    )
