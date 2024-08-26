from django.db import models


class ParentCategory(models.Model):
    name = models.CharField(max_length=200)
    equip_category_id = models.CharField(max_length=200)
    image = models.ImageField(upload_to="./static/images/parent_categories")

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    equip_categroy_id = models.CharField(max_length=200)
    image = models.ImageField(upload_to="./static/images/categories")

    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200)
    equip_model_id = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
