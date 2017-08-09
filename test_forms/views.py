# DJANGO imports
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.edit import FormView

# FORM TOOLS imports
from formtools.wizard.views import SessionWizardView

# LOCAL APP import 
from . import forms
from . import models

# Section 1 view
class Sect1View(FormView):
    template_name = 'test_forms/section.html'
    form_class = forms.Sect1Form
    success_url = 'test_forms:sect2'

    def form_valid(self, form):

        return super(Sect1View, self).form_valid(form)


# Section 2 view
class Sect2View(FormView):
    template_name = 'test_forms/section.html'
    form_class = forms.Sect2Form
    success_url = ''

    def form_valid(self, form):

        return super(Sect2View, self).form_valid(form)

# temporary pdf view
def PDFView(request):
    return render(request, 'test_forms/pdf.html')

#=========================================================
#====================== FORM WIZARD ======================   
#=========================================================

# keep urls clean
TRANSFER_FORMS = [
    ("step1", forms.Section1Form),
    ("step2", forms.Section2Form),
]

# Handle form data
def process_form_data(form_list):
    
    form_data = [form.cleaned_data for form in form_list]

    return form_data

# Complete Test Form wizard view
# Handles form when it is complete
class TestWizard(SessionWizardView):

    # template
    template_name = 'test_forms/test_wizard_form.html'

    # list of forms
    #form_list = [forms.Section1Form, forms.Section2Form]

    def done(self, form_list, **kwargs):
        
        form_data = process_form_data(form_list)

        for form in form_list:
            if request.method == 'post':
                form = form
                if form.is_valid():
                    form = form.cleaned_data['form']
                    form.save(commit=False)
                    file = open("new_file", "a+")
                    file.write(form.property_address)
                    form.save()
                    return form_list
        return render_to_response('form_tests/done.html', {'form_data': form_data})

test_form_wizard_view = TestWizard.as_view(TRANSFER_FORMS)
