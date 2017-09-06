# PYTHON imports
from collections import Counter

# DJANGO imports
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import resolve, reverse, reverse_lazy
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
class IndependentCustomerAddressView(generic.CreateView):
    template_name = 'test_forms/address_check.html'
    form_class = forms.NewCustomerAddressForm
    

# ===================================================================================
# Inspection class
# auto set foreign key relationship
   
class InspectionFormView(FormView):

    template_name = 'test_forms/address_check.html'
    form_class = forms.InspectionForm
    

    def get_initial(self):
        customer_address = get_object_or_404(models.CustomerAddress, slug=self.kwargs['slug'])
        print('customer address: ', customer_address)
        slug = self.kwargs.get('slug')
        print(slug)
        
        inspection = models.Inspection.objects.get(customer_address=customer_address)
        print('inspection: ', inspection)
        global inspection_model
        inspection_model = model_to_dict(inspection)
        print('inspection model: ', inspection_model)
        return inspection_model
    
    def get_success_url(self):
        return reverse('test_form:new-address-form', kwargs={'slug': inspection_model['slug']})


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



#====================================================================================
# Complete Test Form wizard view
# Handles form when it is complete (done method)
class TestWizard(SessionWizardView):

    # template
    template_name = 'test_forms/test_wizard_form.html'


    def get_form_initial(self, step):
        # Grab address from view
        inspection = get_object_or_404(models.Inspection, slug=self.kwargs['slug'])
        #print(address)

        # Query against address to get correct section information \/\/\/
        section_name_list = ['Section1', 'Section2', 'Section3', 'Section4_1', 'Section4_2', 'Section5', 
         'Section6', 'Section7_1', 'Section7_2', 'Section7_3', 'Section7_4', 'Section7_5', 'Section7_6', 
          'Section7_7', 'Section7_9', 'Section8', 'Section9', 'Section10_1', 'Section10_2']
        print(section_name_list)
        section_dictionary_list = []
        section_list_list = []
        global section_list
        
        for section in section_name_list:
            print(section)
            section_dict = section + '_dict'
            section_list = section + '_list'
            section_data = getattr(models, section).objects.get(inspection=inspection, inspection__inspection_date=inspection.inspection_date)
            print('inspection: ', inspection)
            print('inspection date: ', inspection.inspection_date)
            print('section data: ', section_data)
            section_dict = model_to_dict(section_data)
            section_dictionary_list.append(section_dict)
            section_list = list(section_dict.values())
            section_list_list.append(section_list)
        

        for form_dict in section_dictionary_list:
            step_checker = 'step{}'.format(section_dictionary_list.index(form_dict) + 1)
            if step == step_checker:
                return form_dict

    # SAVE TO DB
    def done(self, form_list, form_dict, **kwargs):

        section_done_list = []
        for x in range(1, 21):
            section_done_list.append('section{}'.format(x))

        for section in section_done_list:
            step_number = section_done_list.index(section) + 1
            step = 'step{}'.format(step_number)
            section = form_dict[step].save()
        
        write_on_pdf(section1_list, section2_list)


        return HttpResponseRedirect(reverse('test_form:complete-form'))


# Add clean steps to form wizard
# used in urls.py
TRANSFER_FORMS = [
    ("step1", forms.Section1Form),
    ("step2", forms.Section2Form),
    ("step3", forms.Section3Form),
    ("step4", forms.Section4_1Form),
    ("step5", forms.Section4_2Form),
    ("step6", forms.Section5Form),
    ("step7", forms.Section6Form),
    ("step8", forms.Section7_1Form),
    ("step9", forms.Section7_2Form),
    ("step10", forms.Section7_3Form),
    ("step11", forms.Section7_4Form),
    ("step12", forms.Section7_5Form),
    ("step13", forms.Section7_6Form),
    ("step14", forms.Section7_7Form),
    ("step15", forms.Section7_9Form),
    ("step16", forms.Section8Form),
    ("step17", forms.Section9Form),
    ("step18", forms.Section10_1Form),
    ("step19", forms.Section10_2Form)
]

test_form_wizard_view = TestWizard.as_view(TRANSFER_FORMS)



#====================================================================================
class NewAddressTestWizard(SessionWizardView):

    # template
    template_name = 'test_forms/test_wizard_form.html'

    def form_valid(self, form):
        
        return super(NewAddressTestWizard, self).form_valid(form)

    
    # SAVE TO DB
    def done(self, form_list, form_dict, **kwargs):
        print('working')
        section_done_list = ['Section1']#'Section2', 'Section3', 'Section4_1', 'Section4_2', 'Section5', 
         #'Section6', 'Section7_1', 'Section7_2', 'Section7_3', 'Section7_4', 'Section7_5', 'Section7_6', 
         #'Section7_7', 'Section7_9', 'Section9', 'Section8' 'Section10_1', 'Section10_2']


        for section in section_done_list:
            step_number = section_done_list.index(section) + 1
            step = 'step{}'.format(step_number)
            print(step)
            
            slug = self.kwargs.get('slug')
            print(slug)
            inspection = get_object_or_404(models.Inspection, slug=kwargs['slug'])
            print('goo4: ', inspection)           
            inspection = models.Inspection.objects.get(slug=self.kwargs.get('slug'))
            print('models: ', inspection)
            print(step)
            
            section = form_dict[step].save(commit=False)
            
            section.inspection = inspection
            section.save()
        
        return HttpResponseRedirect(reverse('test_form:device-tests', kwargs={'slug': kwargs['slug']}))

        

tforms = [
    ('step1', forms.Section1Form),
]
new_test_form_wizard_view = NewAddressTestWizard.as_view(tforms)


#=====================================================================================
class DeviceTestFormsetView(generic.CreateView):
    
    
    fields = [
            'device_type',
            'device_address',
            'device_inspection_type',
            'device_inspection_cycle',
            'device_location',
            'device_test_results'
        ]
    formset_class = forms.device_test_formset
    model = models.Section7_8
    queryset = models.Section7_8.objects.none()
    success_url = reverse_lazy('test_form:complete-form')
    template_name = 'test_forms/section.html'

    # def get_context_data(self, **kwargs):
        
    #     data = super(DeviceTestFormsetView, self).get_context_data(**kwargs)
    #     inspection = models.Inspection.objects.get(slug=self.kwargs.get('slug'))
    #     print('models: ', inspection)
    #     data['inspection'] = inspection
    #     return data

    def form_valid(self, form):
        #device_tests = form.save(commit=False)
        inspection = models.Inspection.objects.get(slug=self.kwargs.get('slug'))
        print('models: ', inspection)
        #device_tests.inspection = inspection

        if self.request.method == 'POST':
            print('yo')
            formset = forms.device_test_formset(self.request.POST)
            print('area0')
            if formset.is_valid():
                print('area1')
                for form in formset:
                    print('area2')
                    if form.is_valid():  
                        print('area3')                     
                        instance = form.save(commit=False)
                        print('area4')
                            
            #             instance.inspection = inspection
                            
            #             instance.save()
                            
                        
        #article.save()  # This is redundant, see comments.
        return super(DeviceTestFormsetView, self).form_valid(form)

                   
        


#====================================================================================
# ADDRESS LIST VIEW
class AddressListView(generic.ListView):
    
    context_object_name = 'client_list'
    model = models.CustomerAddress
    queryset = models.CustomerAddress.objects.all()
    template_name = 'test_forms/address_list.html'

        
#====================================================================================            
class TestListView(generic.ListView):

    context_object_name = 'inspection_list'
    model = models.Inspection
    template_name = 'test_forms/test_list.html'

    def get_queryset(self, *args, **kwargs):
        return  models.Inspection.objects.filter(customer_address__slug=self.kwargs['slug'])






    




























