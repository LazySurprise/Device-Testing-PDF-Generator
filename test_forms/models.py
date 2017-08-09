# Create your models here.
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

import datetime

class TestDateTime(models.Model):
    
    tdt_number = models.AutoField(primary_key=True)
    inspection_date = models.DateField(default=datetime.date)
    inspection_time = models.TimeField(default=datetime.time)

class Sect1(models.Model):
    
    ts1_number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    property_name = models.CharField(max_length=10000)
    property_address = models.CharField(max_length=10000)
    property_description = models.CharField(max_length=10000)
    property_representative = models.CharField(max_length=10000)
    pr_address = models.CharField(max_length=10000)
    pr_phone = models.CharField(max_length=10)
    pr_fax = models.CharField(max_length=10)
    pr_email = models.EmailField()
    authority_with_jurisdiction = models.CharField(max_length=10000)
    aj_phone = models.CharField(max_length=10)
    aj_fax = models.CharField(max_length=10)
    aj_email = models.EmailField()

class Sect2(models.Model):

    ts2_number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    org_test_service = models.CharField(max_length=10000)
    ots_address = models.CharField(max_length=10000)
    ots_address = models.CharField(max_length=10000)
    ots_phone = models.CharField(max_length=10)
    ots_fax = models.CharField(max_length=10)
    ots_email = models.EmailField()
    service_technician = models.CharField(max_length=10000)
    test_frequency = models.CharField(max_length=250)
    monitor_org = models.CharField(max_length=10000)
    mo_address = models.CharField(max_length=10000)
    mo_phone = models.CharField(max_length=10)
    mo_fax = models.CharField(max_length=10)
    mo_email = models.EmailField()

class CompleteTest(models.Model):

    test_number = models.AutoField(primary_key=True)
    address = models.CharField(max_length=10000)
    tdt = models.ForeignKey('TestDateTime', null=True)
    sect1 = models.ForeignKey('Sect1', null=True)
    sect2 = models.ForeignKey('Sect2', null=True)


