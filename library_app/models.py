from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    equip_categroy_id = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class EquipmentModel(models.Model):
    equip_model_id = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    equip_model_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="./static/images/model")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.display_name


class LoanLocation(models.Model):
    """for the production purpose"""
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class Loanrequest(models.Model):
    loanrequestid = models.CharField(
        db_column="LoanRequestId", primary_key=True, max_length=50
    )  # Field name made lowercase.
    loanrequestcode = models.CharField(
        db_column="LoanRequestCode", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    loanrequeststatusid = models.CharField(
        db_column="LoanRequestStatusId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    requestedbyid = models.CharField(
        db_column="RequestedById", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    requestdate = models.DateTimeField(
        db_column="RequestDate", blank=True, null=True
    )  # Field name made lowercase.
    categoryid = models.CharField(
        db_column="CategoryId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    modelid = models.CharField(
        db_column="ModelId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    startdate = models.DateTimeField(
        db_column="StartDate", blank=True, null=True
    )  # Field name made lowercase.
    enddate = models.DateTimeField(
        db_column="EndDate", blank=True, null=True
    )  # Field name made lowercase.
    personnelid = models.CharField(
        db_column="PersonnelId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    siteid = models.CharField(
        db_column="SiteId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    locationid = models.CharField(
        db_column="LocationId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    organisationid = models.CharField(
        db_column="OrganisationId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    branchid = models.CharField(
        db_column="BranchId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    teamid = models.CharField(
        db_column="TeamId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    quantity = models.IntegerField(
        db_column="Quantity", blank=True, null=True
    )  # Field name made lowercase.
    loanrequestnotes = models.TextField(
        db_column="LoanRequestNotes", blank=True, null=True
    )  # Field name made lowercase.
    creationdate = models.DateTimeField(
        db_column="CreationDate", blank=True, null=True
    )  # Field name made lowercase.
    modificationdate = models.DateTimeField(
        db_column="ModificationDate", blank=True, null=True
    )  # Field name made lowercase.
    requestedfor = models.CharField(
        db_column="RequestedFor", max_length=255, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "LoanRequest"


class Location(models.Model):
    locationid = models.CharField(
        db_column="LocationId", primary_key=True, max_length=50
    )  # Field name made lowercase.
    locationcode = models.CharField(
        db_column="LocationCode", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    locationshortname = models.CharField(
        db_column="LocationShortName", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    locationlongname = models.TextField(
        db_column="LocationLongName", blank=True, null=True
    )  # Field name made lowercase.
    locationdescription = models.TextField(
        db_column="LocationDescription", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Location"

    def __str__(self) -> str:
        return self.locationshortname
