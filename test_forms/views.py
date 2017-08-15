# PYTHON imports
from collections import Counter

# DJANGO imports
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import resolve, reverse
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.generic.edit import FormView
from django.views import generic

# FORM TOOLS imports
from formtools.wizard.views import SessionWizardView

# LOCAL APP import 
from . import forms
from . import models

# Custom module import
from auto_pdf_2 import write_on_pdf

#====================================================================================
# Grab address for list view
class IndependentCustomerAddressView(FormView):
    template_name = 'test_forms/section.html'
    form_class = forms.CustomerAddressForm

    def form_valid(self, form):

        return super(IndependentCustomerAddressView, self).form_valid(form)

    def post(self):
        
        if self.request == 'POST':
            form = forms.CustomerAddressForm(self.request.POST)
            if form.is_valid():
                form.save()
        else:
            form = forms.CustomerAddressForm

#====================================================================================
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

#====================================================================================
# independent inspection form view
# class IndependentInspectionFormView(FormView):
#     template_name = 'test_forms/section.html'
#     form_class = forms.InspectionForm
#     success_url = 'test_form:test_form_wizard_view'

#     def form_valid(self, form):
        
#         return super(IndependentInspectionFormView, self).form_valid(form)


#     def post(self, request):

#         if self.request == 'POST':

#             form = forms.InspectionForm(self.request.POST)
#             print('form: ', form)
#             print('self.request.post: ', self.request.post)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect(reverse('test_form:test_form_wizard_view'))
#         else:
#             form = forms.InspectionForm
#             return HttpResponseRedirect(reverse('test_form:test_form_wizard_view'))



#====================================================================================
# inspection form view
# class InspectionFormView(FormView):
#     template_name = 'test_forms/test_wizard_form.html'
#     form_class = forms.InspectionForm

    

#     def form_valid(self, form):

#         return super(InspectionFormView, self).form_valid(form)

#     def post(self):
        
        
#         if self.request == 'POST':
#             form = forms.InspectionForm(self.request.POST)
#             print('form: ', form)
#             print('self.request.post: ', self.request.post)
#             if form.is_valid():
#                 form.save()
#         else:
#             form = forms.InspectionForm

#====================================================================================
# inspection form view
# class HiddenInspectionFormView(FormView):
#     template_name = 'test_forms/test_wizard_form.html'
#     form_class = forms.InspectionForm


#====================================================================================
# Section 1 view
class Section1View(FormView):
    template_name = 'test_forms/test_wizard_form.html'
    form_class = forms.Section1Form
    success_url = ''

    def form_valid(self, form):

        form = forms.Section1Form(initial={'property_name': 'test'})
        return super(Section1View, self).form_valid(form)

    def post(self):
        
        if self.request == 'POST':
            form = forms.Section1Form(self.request.POST)
            if form.is_valid():
                form.save()
        else:
            form = forms.Section1Form


#====================================================================================
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

#====================================================================================
# temporary pdf view
def CompleteFormView(request):
    return render(request, 'test_forms/test_form_complete.html')

#=========================================================
#====================== FORM WIZARD ======================   
#=========================================================


#====================================================================================
# Handle form data
def process_form_data(form_list):
    
    form_data = [form.cleaned_data for form in form_list]

    return form_data

TRANSFER_FORMS = [
    ("step1", forms.Section1Form),
    ("step2", forms.Section2Form)
]


#====================================================================================
# Complete Test Form wizard view
# Handles form when it is complete (done method)
class TestWizard(SessionWizardView):

    # template
    template_name = 'test_forms/test_wizard_form.html'

    # def get_form(self, step=None, data=None, files=None):
    #     if step is None:
    #         step = self.steps.current

    #     prev_data = self.get_cleaned_data_for_step(self.get_prev_step(self.steps.current))

    #     if step == '1':
    #         form_class = forms.Section1Form
    #         form = form_class(section1_dict)
    #         print("form works")

    def get_form_initial(self, step):
        address = get_object_or_404(models.CustomerAddress, slug=self.kwargs['slug'])
        # Query against address to get correct section information
        section1 = models.Section1.objects.get(address=address)
        section1_dict = model_to_dict(section1)
        global section1_list
        section1_list = list(section1_dict.values())
        section2 = models.Section2.objects.get(address=address)
        section2_dict = model_to_dict(section2)
        global section2_list
        section2_list = list(section2_dict.values())
        print(section1_list)
        print(section1_list[15])

        print('step: ', step)
        if step == 'step1':
            return section1_dict
        if step == 'step2':
            return section2_dict

    # SAVE TO DB
    def done(self, form_list, form_dict, **kwargs):
        section1 = form_dict['step1'].save()
        section2 = form_dict['step2'].save()
        write_on_pdf(section1_list, section2_list)


        return HttpResponseRedirect(reverse('test_form:complete-form'))


# Add clean steps to form wizard
# used in urls.py
TRANSFER_FORMS = [
    ("step1", forms.Section1Form),
    ("step2", forms.Section2Form)
]

test_form_wizard_view = TestWizard.as_view(TRANSFER_FORMS)



#====================================================================================
class NewAddressTestWizard(SessionWizardView):

    # template
    template_name = 'test_forms/test_wizard_form.html'

    

    # SAVE TO DB
    def done(self, form_list, form_dict, **kwargs):
        print("done method")
        new_customer_address = form_dict['step1'].save()
        print("address saved")
        section1 = form_dict['step2'].save()
        print("sect 1 saved")
        section2 = form_dict['step3'].save()
        print("sect 2 saved")

        return HttpResponseRedirect(reverse('test_form:test-form-complete'))


# Add clean steps to form wizard
# used in urls.py
NEW_TEST_TRANSFER_FORMS = [
    ("step1", forms.CustomerAddressForm),
    ("step2", forms.Section1Form),
    ("step3", forms.Section2Form)
]

new_test_form_wizard_view = TestWizard.as_view(NEW_TEST_TRANSFER_FORMS)


#====================================================================================
# ADDRESS LIST VIEW
class AddressListView(generic.ListView):
    
    context_object_name = 'client_list'
    model = models.CustomerAddress
    queryset = models.CustomerAddress.objects.all()
    template_name = 'test_forms/address_list.html'

    #def get_queryset(self):
     #   return models.CompleteTest.objects.values_list('address', flat=True).distinct()
        
#====================================================================================            
class TestListView(generic.ListView):

    context_object_name = 'inspection_list'
    model = models.Section1
    queryset = models.Section1.objects.all()
    template_name = 'test_forms/test_list.html'


#class AddressDetailView(generic.DetailView):
    
 #   model = models.CompleteTest

  #  template_name = 'test_forms/address_detail.html'



    




























