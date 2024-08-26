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


from django.db import models


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
        managed = True
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
    locationnotes = models.TextField(
        db_column="LocationNotes", blank=True, null=True
    )  # Field name made lowercase.
    locationissuedate = models.DateTimeField(
        db_column="LocationIssueDate", blank=True, null=True
    )  # Field name made lowercase.
    locationversion = models.CharField(
        db_column="LocationVersion", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    ownerid = models.CharField(
        db_column="OwnerId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    groupid = models.CharField(
        db_column="GroupId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    ownerrights = models.SmallIntegerField(
        db_column="OwnerRights", blank=True, null=True
    )  # Field name made lowercase.
    grouprights = models.SmallIntegerField(
        db_column="GroupRights", blank=True, null=True
    )  # Field name made lowercase.
    worldrights = models.SmallIntegerField(
        db_column="WorldRights", blank=True, null=True
    )  # Field name made lowercase.
    siteid = models.CharField(
        db_column="SiteId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    parentid = models.CharField(
        db_column="ParentId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    path = models.TextField(
        db_column="Path", blank=True, null=True
    )  # Field name made lowercase.
    pathname = models.TextField(
        db_column="PathName", blank=True, null=True
    )  # Field name made lowercase.
    address = models.TextField(
        db_column="Address", blank=True, null=True
    )  # Field name made lowercase.
    postcode = models.CharField(
        db_column="PostCode", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    countryid = models.CharField(
        db_column="CountryId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    url = models.CharField(
        db_column="URL", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    email = models.CharField(
        db_column="EMail", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    tel1 = models.CharField(
        db_column="Tel1", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    extn1 = models.CharField(
        db_column="Extn1", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    tel2 = models.CharField(
        db_column="Tel2", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    extn2 = models.CharField(
        db_column="Extn2", max_length=20, blank=True, null=True
    )  # Field name made lowercase.
    fax = models.CharField(
        db_column="Fax", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    mobile1 = models.CharField(
        db_column="Mobile1", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    mobile2 = models.CharField(
        db_column="Mobile2", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    bleep = models.CharField(
        db_column="Bleep", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    contactid = models.CharField(
        db_column="ContactId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    branchid = models.CharField(
        db_column="BranchId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    locationtypeid = models.CharField(
        db_column="LocationTypeId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    teamid = models.CharField(
        db_column="TeamId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    defaultsparepartlocationid = models.CharField(
        db_column="DefaultSparePartLocationId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    customerid = models.CharField(
        db_column="CustomerId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    area = models.FloatField(
        db_column="Area", blank=True, null=True
    )  # Field name made lowercase.
    roomno = models.CharField(
        db_column="RoomNo", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    creationdate = models.DateTimeField(
        db_column="CreationDate", blank=True, null=True
    )  # Field name made lowercase.
    modificationdate = models.DateTimeField(
        db_column="ModificationDate", blank=True, null=True
    )  # Field name made lowercase.
    inactive = models.BooleanField(
        db_column="Inactive", blank=True, null=True
    )  # Field name made lowercase.
    maintenanceweek = models.IntegerField(
        db_column="MaintenanceWeek", blank=True, null=True
    )  # Field name made lowercase.
    lastauditdate = models.DateTimeField(
        db_column="LastAuditDate", blank=True, null=True
    )  # Field name made lowercase.
    annonymouslogin = models.BooleanField(
        db_column="AnnonymousLogin", blank=True, null=True
    )  # Field name made lowercase.
    priorityresponse_high = models.FloatField(
        db_column="PriorityResponse_High", blank=True, null=True
    )  # Field name made lowercase.
    priorityresponse_medium = models.FloatField(
        db_column="PriorityResponse_Medium", blank=True, null=True
    )  # Field name made lowercase.
    priorityresponse_low = models.FloatField(
        db_column="PriorityResponse_Low", blank=True, null=True
    )  # Field name made lowercase.
    priorityturnaround_high = models.FloatField(
        db_column="PriorityTurnaround_High", blank=True, null=True
    )  # Field name made lowercase.
    priorityturnaround_medium = models.FloatField(
        db_column="PriorityTurnaround_Medium", blank=True, null=True
    )  # Field name made lowercase.
    priorityturnaround_low = models.FloatField(
        db_column="PriorityTurnaround_Low", blank=True, null=True
    )  # Field name made lowercase.
    monday = models.BooleanField(
        db_column="Monday", blank=True, null=True
    )  # Field name made lowercase.
    mondaystart = models.DateTimeField(
        db_column="MondayStart", blank=True, null=True
    )  # Field name made lowercase.
    mondayend = models.DateTimeField(
        db_column="MondayEnd", blank=True, null=True
    )  # Field name made lowercase.
    tuesday = models.BooleanField(
        db_column="Tuesday", blank=True, null=True
    )  # Field name made lowercase.
    tuesdaystart = models.DateTimeField(
        db_column="TuesdayStart", blank=True, null=True
    )  # Field name made lowercase.
    tuesdayend = models.DateTimeField(
        db_column="TuesdayEnd", blank=True, null=True
    )  # Field name made lowercase.
    wednesday = models.BooleanField(
        db_column="Wednesday", blank=True, null=True
    )  # Field name made lowercase.
    wednesdaystart = models.DateTimeField(
        db_column="WednesdayStart", blank=True, null=True
    )  # Field name made lowercase.
    wednesdayend = models.DateTimeField(
        db_column="WednesdayEnd", blank=True, null=True
    )  # Field name made lowercase.
    thursday = models.BooleanField(
        db_column="Thursday", blank=True, null=True
    )  # Field name made lowercase.
    thursdaystart = models.DateTimeField(
        db_column="ThursdayStart", blank=True, null=True
    )  # Field name made lowercase.
    thursdayend = models.DateTimeField(
        db_column="ThursdayEnd", blank=True, null=True
    )  # Field name made lowercase.
    friday = models.BooleanField(
        db_column="Friday", blank=True, null=True
    )  # Field name made lowercase.
    fridaystart = models.DateTimeField(
        db_column="FridayStart", blank=True, null=True
    )  # Field name made lowercase.
    fridayend = models.DateTimeField(
        db_column="FridayEnd", blank=True, null=True
    )  # Field name made lowercase.
    saturday = models.BooleanField(
        db_column="Saturday", blank=True, null=True
    )  # Field name made lowercase.
    saturdaystart = models.DateTimeField(
        db_column="SaturdayStart", blank=True, null=True
    )  # Field name made lowercase.
    saturdayend = models.DateTimeField(
        db_column="SaturdayEnd", blank=True, null=True
    )  # Field name made lowercase.
    sunday = models.BooleanField(
        db_column="Sunday", blank=True, null=True
    )  # Field name made lowercase.
    sundaystart = models.DateTimeField(
        db_column="SundayStart", blank=True, null=True
    )  # Field name made lowercase.
    sundayend = models.DateTimeField(
        db_column="SundayEnd", blank=True, null=True
    )  # Field name made lowercase.
    holidays = models.BooleanField(
        db_column="Holidays", blank=True, null=True
    )  # Field name made lowercase.
    holidaystart = models.DateTimeField(
        db_column="HolidayStart", blank=True, null=True
    )  # Field name made lowercase.
    holidayend = models.DateTimeField(
        db_column="HolidayEnd", blank=True, null=True
    )  # Field name made lowercase.
    automanageloans = models.BooleanField(
        db_column="AutoManageLoans", blank=True, null=True
    )  # Field name made lowercase.
    ppmscheduleid = models.CharField(
        db_column="PPMScheduleId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    synchwithrfid = models.BooleanField(
        db_column="SynchWithRFID", blank=True, null=True
    )  # Field name made lowercase.
    synchwithmobiledevice = models.BooleanField(
        db_column="SynchWithMobileDevice", blank=True, null=True
    )  # Field name made lowercase.
    budgetid = models.CharField(
        db_column="BudgetId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    gs1_gln = models.CharField(
        db_column="GS1_GLN", max_length=6, blank=True, null=True
    )  # Field name made lowercase.
    isstocklocation = models.BooleanField(
        db_column="IsStockLocation", blank=True, null=True
    )  # Field name made lowercase.
    trainingadmin1id = models.CharField(
        db_column="TrainingAdmin1Id", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    trainingadmin2id = models.CharField(
        db_column="TrainingAdmin2Id", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    trainingadmin3id = models.CharField(
        db_column="TrainingAdmin3Id", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    trainingadmin4id = models.CharField(
        db_column="TrainingAdmin4Id", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    trainingadmin5id = models.CharField(
        db_column="TrainingAdmin5Id", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    contact = models.CharField(
        db_column="Contact", max_length=255, blank=True, null=True
    )  # Field name made lowercase.
    specialtyid = models.CharField(
        db_column="SpecialtyId", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    maintenancetime = models.FloatField(
        db_column="MaintenanceTime", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Location"

    def __str__(self) -> str:
        return self.locationshortname
