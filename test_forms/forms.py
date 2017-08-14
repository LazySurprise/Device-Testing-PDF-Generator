import itertools

# DJANGO import
from django import forms
from django.utils.text import slugify

# LOCAL APP import
from . import models

#===========================================================================
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings

class RelatedFieldWidgetCanAdd(widgets.Select):

    def __init__(self, related_model, related_url='test_form:new_test_form_wizard_view', *args, **kw):

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

class CustomerAddressForm(forms.ModelForm):

    class Meta:
        model = models.CustomerAddress
        fields = [
            'address',
        ]

class InspectionForm(forms.ModelForm):

    address = forms.ModelChoiceField(
       required=True,
       queryset=models.CustomerAddress.objects.all(),
       widget=RelatedFieldWidgetCanAdd(models.CustomerAddress)
                                )
    class Meta:
       model = models.Inspection
       fields = ('address',)

class Section1Form(forms.ModelForm):

    class Meta:
        model = models.Section1
        exclude = [
            'inspection',
            'ts1_number'
        ]


class Section1FormPreFill(forms.ModelForm):

    class Meta:
        model = models.Section1
        exclude = [
            'inspection',
            'ts1_number'
        ]

    def __init__(self, *args, **kwargs):
            # Get 'initial' argument if any
        initial_arguments = kwargs.get('initial', None)
        updated_initial = {}
        if initial_arguments:
            # We have initial arguments, fetch 'user' placeholder variable if any
            address = initial_arguments.get('',None)
            # Now update the form's initial values if user
            if user:
                updated_initial['property_name'] = getattr(address, 'property_name', None)
                updated_initial['property_address'] = getattr(address, 'property_address', None)
            # You can also initialize form fields with hardcoded values
            # or perform complex DB logic here to then perform initialization
        #updated_initial['comment'] = 'Please provide a comment'
            # Finally update the kwargs initial reference
        kwargs.update(initial=updated_initial)
        super(Section1FormPreFill, self).__init__(*args, **kwargs)
    

class Section2Form(forms.ModelForm):

    class Meta:
        model = models.Section2
        exclude = [
            'inspection',
            'ts2_number',
        ]



    
