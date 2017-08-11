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
class CompleteTestView(FormView):
    template_name = 'test_forms/test_wizard_form.html'
    form_class = forms.CompleteTestForm

    def form_valid(self, form):

        return super(CompleteTestView, self).form_valid(form)

    def post(self):
        
        if self.request == 'POST':
            form = forms.CompleteTestForm(self.request.POST)
            if form.is_valid():
                form.save()
        else:
            form = forms.CompleteTestForm

# Section 1 view

class Sect1View(FormView):
    template_name = 'test_forms/test_wizard_form.html'
    form_class = forms.Sect1Form
    success_url = ''

    def form_valid(self, form):

        return super(Sect1View, self).form_valid(form)

    def post(self):
        
        if self.request == 'POST':
            form = forms.Sect1Form(self.request.POST)
            if form.is_valid():
                form.save()
        else:
            form = forms.Sect1Form


# Section 2 view

class Sect2View(FormView):
    template_name = 'test_forms/test_wizard_form.html'
    form_class = forms.Sect2Form
    success_url = ''

    def form_valid(self, form):

        return super(Sect2View, self).form_valid(form)

    def post(self):
        
        if self.request == 'POST':
            form = forms.Sect2Form(self.request.POST)
            if form.is_valid():
                form.save()
        else:
            form = forms.Sect2Form

# temporary pdf view

def TestFormCompleteView(request):
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
    ("step1", forms.CompleteTestForm),
    ("step2", forms.Sect1Form),
    ("step3", forms.Sect2Form)
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
        complete_test = form_dict['step1'].save()
        print("address saved")
        section1 = form_dict['step2'].save()
        print("sect 1 saved")
        section2 = form_dict['step3'].save()
        print("sect 2 saved")

        return HttpResponseRedirect(reverse('test_form:test-form-complete'))


# Add clean steps to form wizard
# used in urls.py
test_form_wizard_view = TestWizard.as_view(TRANSFER_FORMS)


# ADDRESS LIST VIEW

class AddressListView(generic.ListView):
    
    context_object_name = 'client_list'
    model = models.CompleteTest
    queryset = models.CompleteTest.objects.order_by('-address')
    template_name = 'test_forms/address_list.html'

class AddressDetailView(generic.DetailView):
    
    model = models.CompleteTest

    template_name = 'test_forms/address_detail.html'

    




























