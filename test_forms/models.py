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
    slug = models.SlugField(unique=True, max_length=255)



    def _get_unique_slug(self):
        slug = slugify(self.inspection_date)
        unique_slug = slug
        num = 1
        while Inspection.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    #def get_absolute_url(self):
     #   return reverse('test_forms:address-detail', kwargs={'slug', self.slug})


class Section1(models.Model):
    
    inspection = models.ForeignKey('Inspection', null=True)
    ts1_number = models.AutoField(primary_key=True)
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

class Section2(models.Model):

    inspection = models.ForeignKey('Inspection', null=True)
    ts2_number = models.AutoField(primary_key=True)
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




    

#class CompleteTest(models.Model):

 #   test_number = models.AutoField(primary_key=True)
  #  address = models.CharField(max_length=10000)
   # inspection_date = models.DateField(default=datetime.date.today)
    #inspection_time = models.TimeField(default=datetime.datetime.now().time())
  #  slug = models.SlugField(unique=True, max_length=255)
   # sect1 = models.ForeignKey('Sect1', null=True)
    #sect2 = models.ForeignKey('Sect2', null=True)

    

# def create_address_slug(instance, new_slug=None):
#     slug = slugify(instance.address)
#     if new_slug is not None:
#         slug = new_slug
#     queryset = CustomerAddress.objects.filter(slug=slug).order_by('-customer_pk')
#     exists = queryset.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, queryset.first().customer_pk)
#         return create_address_slug(instance, new_slug=new_slug)
#     return slug

# def pre_save_post_receiver(sender, instance, *args, **kwargs):

#     if not instance.slug:
#         instance.slug = create_address_slug(instance)


# pre_save.connect(pre_save_post_receiver, sender=CustomerAddress)

    

    


