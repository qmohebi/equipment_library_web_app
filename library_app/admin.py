from django.contrib import admin
from .models import Category, EquipmentModel, LoanLocation

admin.site.register(Category)
admin.site.register(EquipmentModel)
admin.site.register(LoanLocation)
