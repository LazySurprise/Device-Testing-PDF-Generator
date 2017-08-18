# DJANGO imports
from django.core.urlresolvers import reverse
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
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
        super(CustomerAddress, self).save(**kwargs)
        inspection = Inspection(customer_address=self)
        inspection.save()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('test_form:address-check', kwargs={'slug': self.slug})



class Inspection(models.Model):

    customer_address = models.ForeignKey(CustomerAddress)
    inspection_date = models.DateField(default=datetime.date.today)
    inspection_time = models.TimeField(default=datetime.datetime.now().time())
    slug = models.SlugField(max_length=140, unique=True)

    def _get_unique_slug(self):
        slug = slugify(self.customer_address) + slugify(self.inspection_date)
        unique_slug = slug
        num = 1
        while Inspection.objects.filter(slug=unique_slug).exists():
            
            unique_slug = '{}-{}'.format(slug, num)
            
            num += 1
        return unique_slug

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('test_form:new-address-form', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Inspection, self).save(**kwargs)

    def __str__(self):
        return str(self.customer_address)

    # def save(self, *args, **kwargs):
    #     instance = super(Inspection, self).save(*args, **kwargs)
    #     self.customer_address.save()
    #     return instance

        # ALL SECTION MODELS
        # section_list = [Section1, Section2, Section3, Section4_1, Section4_2, Section5, 
        # Section6, Section7_1, Section7_2, Section7_3, Section7_4, Section7_5, Section7_6, 
        # Section7_7, Section7_8, Section7_9, Section8, Section9, Section10_1, Section10_2]

        # # all instance variables
        # section_list_lowercase = ['section1', 'section2', 'section3', 'section4_1', 'section4_2', 'section5',
        # 'section6', 'section7_1', 'section7_2', 'section7_3', 'section7_4',
        # 'section7_5', 'section7_6', 'section7_7', 'section7_8', 'section7_9', 'section8',
        # 'section9', 'section10_1', 'section10_2']
        
        # # SET ALL SECTION MODELS FOREIGN KEY
        # # RELATIONSHIP WITH INSPECTION
        # for section, section_lowercased in zip(section_list, section_list_lowercase):
        #     section_lowercased = section(inspection=self)
        #     section_lowercased.save()

    
        #section1 = Section1(inspection=self)
        #section1.save()

    # def __unicode__(self):

    #     return unicode(self.customer_address)



    # # ==============================================================================
    # @receiver(post_save,sender=CustomerAddress)
    # def my_handler(sender,instance,**kwargs):
    #     p=Inspection(customer_address_id=instance.customer_pk)
    #     p.save()
    # ==============================================================================


class Section1(models.Model):
    
    inspection = models.ForeignKey(Inspection)
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

    def __str__(self):
        admin_name = str(self.inspection) + '-section1'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section1, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section2(models.Model):

    inspection = models.ForeignKey(Inspection)
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

    def __str__(self):
        admin_name = str(self.inspection) + '-section2'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section2, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section3(models.Model):

    inspection = models.ForeignKey(Inspection)
    fas_nonvoice = models.BooleanField(default=False)
    evacs = models.BooleanField(default=False)
    mns = models.BooleanField(default=False)
    system_combo = models.BooleanField(default=False)
    fas_nonvoice_combo = models.BooleanField(default=False)
    evacs_combo = models.BooleanField(default=False)
    mns_combo = models.BooleanField(default=False)
    two_way_combo = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    specify = models.CharField(max_length=10000, null=True, blank=True)
    manufacturer = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255)
    sys_docs = models.BooleanField(default=False)
    sys_docs_location = models.CharField(max_length=500, null=True, blank=True)
    site_specific_software = models.BooleanField(default=False)
    revision_number = models.CharField(max_length=255, null=True, blank=True)
    last_update = models.DateField(default=None, null=True, blank=True)
    site_software_copy = models.BooleanField(default=False)
    copy_location = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section3'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section3, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section4_1(models.Model):

    inspection = models.ForeignKey(Inspection)
    cp_input_voltage = models.FloatField(max_length=255)
    cp_amps = models.FloatField(max_length=255)
    generator = models.BooleanField(default=False)
    generator_location = models.CharField(max_length=10000, null=True, blank=True)
    generator_fuel_location = models.CharField(max_length=500, null=True, blank=True)
    generator_fuel_type = models.CharField(max_length=255, null=True, blank=True)
    ups = models.BooleanField(default=False)
    ups_powered_equipment = models.CharField(max_length=10000, null=True, blank=True)
    ups_location = models.CharField(max_length=10000, null=True, blank=True)
    ups_battery_standby = models.FloatField(max_length=255, null=True, blank=True)
    ups_battery_alarm = models.FloatField(max_length=255, null=True, blank=True)
    battery_location = models.CharField(max_length=100)
    battery_type = models.CharField(max_length=100)
    battery_voltage = models.FloatField(max_length=100)
    battery_amp_hour = models.CharField(max_length=100)
    battery_standby = models.FloatField(max_length=100)
    battery_alarm = models.FloatField(max_length=100)
    battery_mark = models.BooleanField(default=False)

    def __str__(self):
        admin_name = str(self.inspection) + '-section4_1'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section4_1, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section4_2(models.Model):

    inspection = models.ForeignKey(Inspection)
    power_extender_panels = models.BooleanField(default=False)
    pep_voltage = models.FloatField(max_length=255, null=True, blank=True)
    pep_amps = models.FloatField(max_length=255, null=True, blank=True)
    generator = models.BooleanField(default=False)
    generator_location = models.CharField(max_length=10000, null=True, blank=True)
    generator_fuel_location = models.CharField(max_length=500, null=True, blank=True)
    generator_fuel_type = models.CharField(max_length=255, null=True, blank=True)
    ups = models.BooleanField(default=False)
    ups_powered_equipment = models.CharField(max_length=10000, null=True, blank=True)
    ups_location = models.CharField(max_length=10000, null=True, blank=True)
    ups_battery_standby = models.FloatField(max_length=255, null=True, blank=True)
    ups_battery_alarm = models.FloatField(max_length=255, null=True, blank=True)
    battery_location = models.CharField(max_length=100)
    battery_type = models.CharField(max_length=100)
    battery_voltage = models.FloatField(max_length=100)
    battery_amp_hour = models.CharField(max_length=100)
    battery_standby = models.FloatField(max_length=100)
    battery_alarm = models.FloatField(max_length=100)
    battery_mark = models.BooleanField(default=False)

    def __str__(self):
        admin_name = str(self.inspection) + '-section4_2'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section4_2, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section5(models.Model):

    inspection = models.ForeignKey(Inspection)
    anunciators = models.BooleanField(default=False)
    anunciator1 = models.CharField(max_length=10000, null=True, blank=True)
    anunciator2 = models.CharField(max_length=10000, null=True, blank=True)
    anunciator3 = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section5'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section5, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section6(models.Model):

    inspection = models.ForeignKey(Inspection)
    monitor_contact = models.CharField(max_length=10000, null=True, blank=True)
    monitor_time = models.CharField(max_length=10000, null=True, blank=True)
    management_contact = models.CharField(max_length=10000, null=True, blank=True)
    management_time = models.CharField(max_length=10000, null=True, blank=True)
    occupant_contact = models.CharField(max_length=10000, null=True, blank=True)
    occupant_time = models.CharField(max_length=10000, null=True, blank=True)
    authority_contact = models.CharField(max_length=10000, null=True, blank=True)
    authority_time = models.CharField(max_length=10000, null=True, blank=True)
    other_contact = models.CharField(max_length=10000, null=True, blank=True)
    other_time = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section6'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section6, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section7_1(models.Model):

    inspection = models.ForeignKey(Inspection)
    cu_vi = models.BooleanField(default=False)
    cu_ft = models.BooleanField(default=False)
    cu_comments = models.CharField(max_length=10000, null=True, blank=True)
    lighting_vi = models.BooleanField(default=False)
    lighting_ft = models.BooleanField(default=False)
    lighting_comments = models.CharField(max_length=10000, null=True, blank=True)
    fuse_vi = models.BooleanField(default=False)
    fuse_ft = models.BooleanField(default=False)
    fuse_comments = models.CharField(max_length=10000, null=True, blank=True)
    trouble_signal_vi = models.BooleanField(default=False)
    trouble_signal_ft = models.BooleanField(default=False)
    trouble_signal_comments = models.CharField(max_length=10000, null=True, blank=True)
    disconnect_switches_vi = models.BooleanField(default=False)
    disconnect_switches_ft = models.BooleanField(default=False)
    disconnect_switches_comments = models.CharField(max_length=10000, null=True, blank=True)
    gf_monitoring_vi = models.BooleanField(default=False)
    gf_monitoring_ft = models.BooleanField(default=False)
    gf_monitoring_comments = models.CharField(max_length=10000, null=True, blank=True)
    supervision_vi = models.BooleanField(default=False)
    supervision_ft = models.BooleanField(default=False)
    supervision_comments = models.CharField(max_length=10000, null=True, blank=True)
    local_annunciator_vi = models.BooleanField(default=False)
    local_annunciator_ft = models.BooleanField(default=False)
    local_annunciator_comments = models.CharField(max_length=10000, null=True, blank=True)
    remote_annunciator_vi = models.BooleanField(default=False)
    remote_annunciator_ft = models.BooleanField(default=False)
    remote_annunciator_comments = models.CharField(max_length=10000, null=True, blank=True)
    pep_vi = models.BooleanField(default=False)
    pep_ft = models.BooleanField(default=False)
    pep_comments = models.CharField(max_length=10000, null=True, blank=True)
    iso_mods_vi = models.BooleanField(default=False)
    iso_mods_ft = models.BooleanField(default=False)
    iso_mod_comments = models.CharField(max_length=10000, null=True, blank=True)
    other_vi = models.BooleanField(default=False)
    other_ft = models.BooleanField(default=False)
    other_comments = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section7_1'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section7_1, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section7_2(models.Model):

    inspection = models.ForeignKey(Inspection)
    volt_120_vi = models.BooleanField(default=False)
    volt_120_ft = models.BooleanField(default=False)
    volt_120_comments = models.CharField(max_length=10000, null=True, blank=True)
    generator_ups_vi = models.BooleanField(default=False)
    generator_ups_ft = models.BooleanField(default=False)
    generatorcomments = models.CharField(max_length=10000, null=True, blank=True)
    battery_condition_vi = models.BooleanField(default=False)
    battery_condition_ft = models.BooleanField(default=False)
    battery_condition_comments = models.CharField(max_length=10000, null=True, blank=True)
    load_voltage_vi = models.BooleanField(default=False)
    load_voltage_ft = models.BooleanField(default=False)
    load_voltage_comments = models.CharField(max_length=10000, null=True, blank=True)
    discharge_vi = models.BooleanField(default=False)
    discharge_ft = models.BooleanField(default=False)
    discharge_comments = models.CharField(max_length=10000, null=True, blank=True)
    charger_vi = models.BooleanField(default=False)
    charger_ft = models.BooleanField(default=False)
    charger_comments = models.CharField(max_length=10000, null=True, blank=True)
    other_vi = models.BooleanField(default=False)
    other_ft = models.BooleanField(default=False)
    other_comments = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section7_2'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section7_2, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section7_3(models.Model):

    inspection = models.ForeignKey(Inspection)
    light_vi = models.BooleanField(default=False)
    light_ft = models.BooleanField(default=False)
    light_comments = models.CharField(max_length=10000, null=True, blank=True)
    fuse_vi = models.BooleanField(default=False)
    fuse_ft = models.BooleanField(default=False)
    fuse_comments = models.CharField(max_length=10000, null=True, blank=True)
    primary_power_vi = models.BooleanField(default=False)
    primary_power_ft = models.BooleanField(default=False)
    primary_power_comments = models.CharField(max_length=10000, null=True, blank=True)
    secondary_power_vi = models.BooleanField(default=False)
    secondary_power_ft = models.BooleanField(default=False)
    secondary_power_comments = models.CharField(max_length=10000, null=True, blank=True)
    trouble_signals_vi = models.BooleanField(default=False)
    trouble_signals_ft = models.BooleanField(default=False)
    trouble_signals_comments = models.CharField(max_length=10000, null=True, blank=True)
    gf_monitoring_vi = models.BooleanField(default=False)
    gf_monitoring_ft = models.BooleanField(default=False)
    gf_monitoring_comments = models.CharField(max_length=10000, null=True, blank=True)
    panel_super_vi = models.BooleanField(default=False)
    panel_super_ft = models.BooleanField(default=False)
    panel_super_comments = models.CharField(max_length=10000, null=True, blank=True)
    other_vi = models.BooleanField(default=False)
    other_ft = models.BooleanField(default=False)
    other_comments = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section7_3'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section7_3, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section7_4(models.Model):

    inspection = models.ForeignKey(Inspection)
    femds_vi = models.BooleanField(default=False)
    femds_ft = models.BooleanField(default=False)
    femds_comments = models.CharField(max_length=10000, null=True, blank=True)
    cmds_vi = models.BooleanField(default=False)
    cmds_ft = models.BooleanField(default=False)
    cmds_comments = models.CharField(max_length=10000, null=True, blank=True)
    combo_fs_vi = models.BooleanField(default=False)
    combo_fs_ft = models.BooleanField(default=False)
    combo_fs_comments = models.CharField(max_length=10000, null=True, blank=True)
    other_vi = models.BooleanField(default=False)
    other_ft = models.BooleanField(default=False)
    other_comments = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section7_4'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section7_4, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section7_5(models.Model):

    inspection = models.ForeignKey(Inspection)
    shs_1_description = models.CharField(max_length=1000, null=True, blank=True)
    shs_1_vi = models.BooleanField(default=False)
    shs_1_ft = models.BooleanField(default=False)
    shs_1_comment = models.CharField(max_length=1000, null=True, blank=True)
    shs_2_description = models.CharField(max_length=1000, null=True, blank=True)
    shs_2_vi = models.BooleanField(default=False)
    shs_2_ft = models.BooleanField(default=False)
    shs_2_comment = models.CharField(max_length=1000, null=True, blank=True)
    shs_3_description = models.CharField(max_length=1000, null=True, blank=True)
    shs_3_vi = models.BooleanField(default=False)
    shs_3_ft = models.BooleanField(default=False)
    shs_3_comment = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section7_5'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section7_5, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section7_6(models.Model):

    inspection = models.ForeignKey(Inspection)
    generator_vi = models.BooleanField(default=False)
    generator_ft = models.BooleanField(default=False)
    generator_comments = models.CharField(max_length=10000, null=True, blank=True)
    fire_pump_vi = models.BooleanField(default=False)
    fire_pump_ft = models.BooleanField(default=False)
    fire_pump_comments = models.CharField(max_length=10000, null=True, blank=True)
    sus_vi = models.BooleanField(default=False)
    sus_ft = models.BooleanField(default=False)
    sus_comments = models.CharField(max_length=10000, null=True, blank=True)
    other_vi = models.BooleanField(default=False)
    other_ft = models.BooleanField(default=False)
    other_comments = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section7_6'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section7_6, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section7_7(models.Model):

    inspection = models.ForeignKey(Inspection)
    door_releasing_devices_vi = models.BooleanField(default=False)
    door_releasing_devices_ft = models.BooleanField(default=False)
    door_releasing_devices_comments = models.CharField(max_length=10000, null=True, blank=True)
    fan_shutdown_vi = models.BooleanField(default=False)
    fan_shutdown_ft = models.BooleanField(default=False)
    fan_shutdown_comments = models.CharField(max_length=10000, null=True, blank=True)
    smoke_control_vi = models.BooleanField(default=False)
    smoke_control_ft = models.BooleanField(default=False)
    smoke_control_comments = models.CharField(max_length=10000, null=True, blank=True)
    smoke_damper_vi = models.BooleanField(default=False)
    smoke_damper_ft = models.BooleanField(default=False)
    smoke_damper_comments = models.CharField(max_length=10000, null=True, blank=True)
    smoke_shutter_vi = models.BooleanField(default=False)
    smoke_shutter_ft = models.BooleanField(default=False)
    smoke_shutter_comments = models.CharField(max_length=10000, null=True, blank=True)
    door_unlocking_vi = models.BooleanField(default=False)
    door_unlocking_ft = models.BooleanField(default=False)
    door_unlocking_comments = models.CharField(max_length=10000, null=True, blank=True)
    elevator_recall_vi = models.BooleanField(default=False)
    elevator_recall_ft = models.BooleanField(default=False)
    elevator_recall_comments = models.CharField(max_length=10000, null=True, blank=True)
    elevator_shunt_trip_vi = models.BooleanField(default=False)
    elevator_shunt_trip_ft = models.BooleanField(default=False)
    elevator_shunt_trip_comments = models.CharField(max_length=10000, null=True, blank=True)
    other_vi = models.BooleanField(default=False)
    other_ft = models.BooleanField(default=False)
    other_comments = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section7_7'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section7_7, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section7_8(models.Model):

    INSPECTION_CHOICES = (
        ('V', 'Visual Inspection'),
        ('F', 'Functional Test')
    )

    inspection = models.ForeignKey(Inspection)
    device_type = models.CharField(max_length=100)
    device_address = models.CharField(max_length=100)
    device_inspection_type = models.CharField(max_length=1, choices=INSPECTION_CHOICES)
    device_inspection_cycle = models.CharField(max_length=5)
    device_location = models.CharField(max_length=1000)
    device_test_results = models.CharField(max_length=255)

    def __str__(self):
        admin_name = str(self.inspection) + '-section7_8'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section7_8, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section7_9(models.Model):

    inspection = models.ForeignKey(Inspection)
    alarm_signal_vi = models.BooleanField(default=False)
    alarm_signal_ft = models.BooleanField(default=False)
    alarm_signal_time = models.FloatField(max_length=30, null=True, blank=True)
    alarm_signal_comments = models.CharField(max_length=10000, null=True, blank=True)
    alarm_restoration_vi = models.BooleanField(default=False)
    alarm_restoration_ft = models.BooleanField(default=False)
    alarm_restoration_time = models.FloatField(max_length=30, null=True, blank=True)
    alarm_restoration_comments = models.CharField(max_length=10000, null=True, blank=True)
    trouble_signal_vi = models.BooleanField(default=False)
    trouble_signal_ft = models.BooleanField(default=False)
    trouble_signal_time = models.FloatField(max_length=30, null=True, blank=True)
    trouble_signal_comments = models.CharField(max_length=10000, null=True, blank=True)
    trouble_restoration_vi = models.BooleanField(default=False)
    trouble_restoration_ft = models.BooleanField(default=False)
    trouble_restoration_time = models.FloatField(max_length=30, null=True, blank=True)
    trouble_restoration_comments = models.CharField(max_length=10000, null=True, blank=True)
    supervisory_signal_vi = models.BooleanField(default=False)
    supervisory_signal_ft = models.BooleanField(default=False)
    supervisory_signal_time = models.FloatField(max_length=30, null=True, blank=True)
    supervisory_signal_comments = models.CharField(max_length=10000, null=True, blank=True)
    supervisory_restoration_vi = models.BooleanField(default=False)
    supervisory_restoration_ft = models.BooleanField(default=False)
    supervisory_restoration_time = models.FloatField(max_length=30, null=True, blank=True)
    supervisory_restoration_comments = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section7_9'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section7_9, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section8(models.Model):

    inspection = models.ForeignKey(Inspection)
    monitor_contact = models.CharField(max_length=10000, null=True, blank=True)
    monitor_time = models.CharField(max_length=10000, null=True, blank=True)
    management_contact = models.CharField(max_length=10000, null=True, blank=True)
    management_time = models.CharField(max_length=10000, null=True, blank=True)
    occupant_contact = models.CharField(max_length=10000, null=True, blank=True)
    occupant_time = models.CharField(max_length=10000, null=True, blank=True)
    authority_contact = models.CharField(max_length=10000, null=True, blank=True)
    authority_time = models.CharField(max_length=10000, null=True, blank=True)
    other_contact = models.CharField(max_length=10000, null=True, blank=True)
    other_time = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section8'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section8, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section9(models.Model):

    inspection = models.ForeignKey(Inspection)
    system_restore_date = models.DateField(auto_now_add=True)
    system_restore_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        admin_name = str(self.inspection) + '-section9'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section9, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section10_1(models.Model):

    inspection = models.ForeignKey(Inspection)
    inspector_signature = models.CharField(max_length=255)
    inspector_name = models.CharField(max_length=255)
    inspector_organization = models.CharField(max_length=255)
    inspector_title = models.CharField(max_length=255)
    inspector_phone = models.CharField(max_length=10)

    def __str__(self):
        admin_name = str(self.inspection) + '-section10_1'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section10_1, self).save(*args, **kwargs)
        self.inspection.save()
        return instance

class Section10_2(models.Model):

    inspection = models.ForeignKey(Inspection)
    owner_signature = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    owner_date = models.DateField(auto_now_add=True)
    owner_organization = models.CharField(max_length=255)
    owner_title = models.CharField(max_length=255)
    owner_phone = models.CharField(max_length=10)

    def __str__(self):
        admin_name = str(self.inspection) + '-section10_2'
        return admin_name

    def save(self, *args, **kwargs):
        instance = super(Section10_2, self).save(*args, **kwargs)
        self.inspection.save()
        return instance




    

    


