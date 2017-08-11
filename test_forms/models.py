# DJANGO imports
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# PYTHON imports
import datetime
import itertools

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
    inspection_date = models.DateField(default=datetime.date.today)
    inspection_time = models.TimeField(default=datetime.datetime.now().time())
    slug = models.SlugField(unique=True, max_length=255)
    sect1 = models.ForeignKey('Sect1', null=True)
    sect2 = models.ForeignKey('Sect2', null=True)

    def get_absolute_url(self):
        return reverse('test_forms:address-detail', kwargs={'slug', self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.address) + slugify(instance.inspection_date)
    if new_slug is not None:
        slug = new_slug
    queryset = CompleteTest.objects.filter(slug=slug).order_by('-test_number')
    exists = queryset.exists()
    if exists:
        new_slug = "%s-%s" %(slug, queryset.first().test_number)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):

    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=CompleteTest)

    

    


