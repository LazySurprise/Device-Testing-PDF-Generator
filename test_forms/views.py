# PYTHON imports
from collections import Counter

# DJANGO imports
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.generic.edit import FormView
from django.views import generic

# FORM TOOLS imports
from formtools.wizard.views import SessionWizardView

# LOCAL APP import 
from . import forms
from . import models

# complete test
# Grab address for list view
class CustomerAddressView(FormView):
    template_name = 'test_forms/test_wizard_form.html'
    form_class = forms.CustomerAddressForm

    def form_valid(self, form):

        return super(CustomerAddressView, self).form_valid(form)

    def post(self):
        
        if self.request == 'POST':
            form = forms.CustomerAddressForm(self.request.POST)
            if form.is_valid():
                form.save()
        else:
            form = forms.CustomerAddressForm

# inspection form view
class InspectionFormView(FormView):
    template_name = 'test_forms/test_wizard_form.html'
    form_class = forms.InspectionForm

    

    def form_valid(self, form):

        return super(InspectionFormView, self).form_valid(form)

    def post(self):
        
        
        if self.request == 'POST':
            form = forms.InspectionForm(self.request.POST)
            if form.is_valid():
                form.save()

            # try to pre populate
            #try: 
             #   address = models.CustomerAddress.objects.get(address=self.request.address)
                
 


        else:
            form = forms.InspectionForm

# inspection form view
class HiddenInspectionFormView(FormView):
    template_name = 'test_forms/test_wizard_form.html'
    form_class = forms.InspectionForm


# Section 1 view

class Section1View(FormView):
    template_name = 'test_forms/test_wizard_form.html'
    form_class = forms.Section1Form
    success_url = ''

    def form_valid(self, form):

        return super(Section1View, self).form_valid(form)

    def post(self):
        
        if self.request == 'POST':
            form = forms.Section1Form(self.request.POST)
            if form.is_valid():
                form.save()
        else:
            form = forms.Section1Form


# Section 2 view

class Section2View(FormView):
    template_name = 'test_forms/test_wizard_form.html'
    form_class = forms.Section2Form
    success_url = ''

    def form_valid(self, form):

        return super(Section2View, self).form_valid(form)

    def post(self):
        
        if self.request == 'POST':
            form = forms.Section2Form(self.request.POST)
            if form.is_valid():
                form.save()
        else:
            form = forms.Section2Form

# temporary pdf view

def CompleteFormView(request):
    return render(request, 'test_forms/test_form_complete.html')

#=========================================================
#====================== FORM WIZARD ======================   
#=========================================================



# Handle form data
def process_form_data(form_list):
    
    form_data = [form.cleaned_data for form in form_list]

    return form_data

# KEEP steps CLEAN
TRANSFER_FORMS = [
    ("step1", forms.InspectionForm),
    ("step2", forms.Section1FormPreFill),
    ("step3", forms.Section2Form)
]

# Complete Test Form wizard view
# Handles form when it is complete (done method)
class TestWizard(SessionWizardView):

    # template
    template_name = 'test_forms/test_wizard_form.html'

    # list of forms
    #form_list = []

    # SAVE TO DB
    def done(self, form_list, form_dict, **kwargs):
        print("done method")
        print("address saved")
        inspection = form_dict['step1'].save()
        print("address saved")
        section1 = form_dict['step2'].save()
        print("sect 1 saved")
        section2 = form_dict['step3'].save()
        print("sect 2 saved")

        return HttpResponseRedirect(reverse('test_form:complete-form'))


# Add clean steps to form wizard
# used in urls.py
test_form_wizard_view = TestWizard.as_view(TRANSFER_FORMS)

NEW_TEST_TRANSFER_FORMS = [
    ("step1", forms.CustomerAddressForm),
    ("step2", forms.Section1Form),
    ("step3", forms.Section2Form)
]

class NewAddressTestWizard(SessionWizardView):

    # template
    template_name = 'test_forms/test_wizard_form.html'

    # list of forms
    #form_list = []

    # SAVE TO DB
    def done(self, form_list, form_dict, **kwargs):
        print("done method")
        customer_address = form_dict['step1'].save()
        print("address saved")
        section1 = form_dict['step2'].save()
        print("sect 1 saved")
        section2 = form_dict['step3'].save()
        print("sect 2 saved")

        return HttpResponseRedirect(reverse('test_form:test-form-complete'))


# Add clean steps to form wizard
# used in urls.py
new_test_form_wizard_view = TestWizard.as_view(NEW_TEST_TRANSFER_FORMS)


# ADDRESS LIST VIEW

class AddressListView(generic.ListView):
    
    context_object_name = 'client_list'
    model = models.CustomerAddress
    queryset = models.CustomerAddress.objects.all()
    template_name = 'test_forms/address_list.html'

    #def get_queryset(self):
     #   return models.CompleteTest.objects.values_list('address', flat=True).distinct()
        
            
class TestListView(generic.ListView):

    context_object_name = 'inspection_list'
    model = models.Inspection
    queryset = models.Inspection.objects.all()
    template_name = 'test_forms/test_list.html'

#class AddressDetailView(generic.DetailView):
    
 #   model = models.CompleteTest

  #  template_name = 'test_forms/address_detail.html'



    




























