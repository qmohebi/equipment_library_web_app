# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Loanrequest(models.Model):
    loanrequestid = models.CharField(db_column='LoanRequestId', primary_key=True, max_length=50)  # Field name made lowercase.
    loanrequestcode = models.CharField(db_column='LoanRequestCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    loanrequeststatusid = models.CharField(db_column='LoanRequestStatusId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    requestedbyid = models.CharField(db_column='RequestedById', max_length=50, blank=True, null=True)  # Field name made lowercase.
    requestdate = models.DateTimeField(db_column='RequestDate', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modelid = models.CharField(db_column='ModelId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    personnelid = models.CharField(db_column='PersonnelId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locationid = models.CharField(db_column='LocationId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    organisationid = models.CharField(db_column='OrganisationId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchid = models.CharField(db_column='BranchId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    teamid = models.CharField(db_column='TeamId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    loanrequestnotes = models.TextField(db_column='LoanRequestNotes', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.
    requestedfor = models.CharField(db_column='RequestedFor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoanRequest'
