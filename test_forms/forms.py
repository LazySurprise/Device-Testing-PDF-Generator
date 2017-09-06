import itertools

# DJANGO import
from django import forms
from django.forms import modelformset_factory
from django.utils.text import slugify

# LOCAL APP import
from . import models

#===========================================================================
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings

class RelatedFieldWidgetCanAdd(widgets.Select):

    def __init__(self, related_model, related_url='test_form:new-address', *args, **kw):

        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = 'admin:%s_%s_add' % info

        # Be careful that here "reverse" is not allowed
        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = [super(RelatedFieldWidgetCanAdd, self).render(name, value, *args, **kwargs)]
        output.append(u'<a href="%s" class="add-another" id="add_id_%s" onclick="return showAddAnotherPopup(this);"> ' % \
            (self.related_url, name))
        output.append(u'<img src="%sadmin/img/icon_addlink.gif" width="10" height="10" alt="%s"/></a>' % (settings.STATIC_URL, ('Add New Address')))                                                                                                                               
        return mark_safe(u''.join(output))

#===========================================================================

class NewCustomerAddressForm(forms.ModelForm):

    class Meta:
        model = models.CustomerAddress
        fields = [
            'address',
        ]

# ==========================================================================

class InspectionForm(forms.ModelForm):

    class Meta:
        model = models.Inspection
        fields = [
           'customer_address',
        ]

    # the request is now available, add it to the instance data
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(InspectionForm, self).__init__(*args, **kwargs)

#===========================================================================

class CustomerAddressForm(forms.ModelForm):

    address = forms.ModelChoiceField(
       required=True,
       queryset=models.CustomerAddress.objects.all(),
       widget=RelatedFieldWidgetCanAdd(models.CustomerAddress)
    )

    class Meta:
        model = models.CustomerAddress
        fields = [
            'address',
        ]

    # def __init__(self, *args, **kwargs):
    #     super(models.CustomerAddress, self.).save(**kwargs)
    #     inspection = models.Inspection(customer_address=self)
    #     inspection.save()
    


class Section1Form(forms.ModelForm):

    class Meta:
        model = models.Section1
        exclude = [
            'inspection',
        ]

class Section2Form(forms.ModelForm):

    class Meta:
        model = models.Section2
        exclude = [
            'inspection',
        ]

class Section3Form(forms.ModelForm):

    class Meta:
        model = models.Section3
        exclude = [
            'inspection',
        ]

class Section4_1Form(forms.ModelForm):

    class Meta:
        model = models.Section4_1
        exclude = [
            'inspection',
        ]

class Section4_2Form(forms.ModelForm):

    class Meta:
        model = models.Section4_2
        exclude = [
            'inspection',
        ]

class Section5Form(forms.ModelForm):

    class Meta:
        model = models.Section5
        exclude = [
            'inspection',
        ]

class Section6Form(forms.ModelForm):

    class Meta:
        model = models.Section6
        exclude = [
            'inspection',
        ]

class Section7_1Form(forms.ModelForm):

    class Meta:
        model = models.Section7_1
        exclude = [
            'inspection',
        ]

class Section7_2Form(forms.ModelForm):

    class Meta:
        model = models.Section7_2
        exclude = [
            'inspection',
        ]

class Section7_3Form(forms.ModelForm):

    class Meta:
        model = models.Section7_3
        exclude = [
            'inspection',
        ]  

class Section7_4Form(forms.ModelForm):

    class Meta:
        model = models.Section7_4
        exclude = [
            'inspection',
        ]

class Section7_5Form(forms.ModelForm):

    class Meta:
        model = models.Section7_5
        exclude = [
            'inspection',
        ]
class Section7_6Form(forms.ModelForm):

    class Meta:
        model = models.Section7_6
        exclude = [
            'inspection',
        ]

class Section7_7Form(forms.ModelForm):

    class Meta:
        model = models.Section7_7
        exclude = [
            'inspection',
        ]

class Section7_8Form(forms.ModelForm):

    class Meta:
        model = models.Section7_8
        exclude = [
            'inspection',
        ]

device_test_formset = modelformset_factory(
    models.Section7_8,
    form=Section7_8Form,
    extra=20,
    )

#formset = device_test_formset(queryset=models.Section7_8.objects.none())

class Section7_9Form(forms.ModelForm):

    class Meta:
        model = models.Section7_9
        exclude = [
            'inspection',
        ]

class Section8Form(forms.ModelForm):

    class Meta:
        model = models.Section8
        exclude = [
            'inspection',
        ]

class Section9Form(forms.ModelForm):

    class Meta:
        model = models.Section9
        exclude = [
            'inspection',
        ]

class Section10_1Form(forms.ModelForm):

    class Meta:
        model = models.Section10_1
        exclude = [
            'inspection',
        ]

class Section10_2Form(forms.ModelForm):

    class Meta:
        model = models.Section10_2
        exclude = [
            'inspection',
        ]

