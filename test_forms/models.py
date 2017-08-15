# DJANGO imports
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# PYTHON imports
import datetime
import itertools

#======================================================================================
#=========================== DATA MODELS START HERE ===================================

class CustomerAddress(models.Model):
    
    customer_pk = models.AutoField(primary_key=True)
    address = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=140, unique=True)

    def __str__(self):
        return self.address
 
    def _get_unique_slug(self):
        slug = slugify(self.address)
        unique_slug = slug
        num = 1
        while CustomerAddress.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    #def get_absolute_url(self):
     #   return reverse('test_forms:address-detail', kwargs={'slug', self.slug})

class Inspection(models.Model):

    address = models.ForeignKey('CustomerAddress', null=True)
    inspection_number = models.AutoField(primary_key=True)
    inspection_date = models.DateField(default=datetime.date.today)
    inspection_time = models.TimeField(default=datetime.datetime.now().time())
    # slug = models.SlugField(unique=True, max_length=255)

    class Meta:
        abstract = True

    # def _get_unique_slug(self):
    #     slug = slugify(self.address) + slugify(self.inspection_date)
    #     unique_slug = slug
    #     num = 1
    #     while Inspection.objects.filter(slug=unique_slug).exists():
    #         unique_slug = '{}-{}'.format(slug, num)
    #         num += 1
    #     return unique_slug
 
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = self._get_unique_slug()
    #     super().save()

    #def get_absolute_url(self):
     #   return reverse('test_forms:address-detail', kwargs={'slug', self.slug})


class Section1(Inspection):
    
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

class Section2(Inspection):

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



    

    


