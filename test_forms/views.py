# DJANGO imports
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

# FORM TOOLS imports
from formtools.wizard.views import SessionWizardView

# LOCAL APP import 
from . import forms
from . import models

# complete test
# Grab address for list view
class CompleteTestView(FormView):
    template_name = 'test_forms/section.html'
    form_class = forms.CompleteTestForm

    def form_valid(self, form):

        return super(CompleteTestView, self).form_valid(form)

# Section 1 view
class Sect1View(FormView):
    template_name = 'test_forms/section.html'
    form_class = forms.Sect1Form
    success_url = ''

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
def TestFormCompleteView(request):
    return render(request, 'test_forms/test_form_complete.html')

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
            if self.request.method == 'post':
                form = form
                if form.is_valid():
                    form = form.cleaned_data['form']
                    form.save(commit=False)
                    file = open("new_file", "a+")
                    file.write(form.property_address)
                    form.save()
                    return form_list
        return render_to_response('test_forms/test_form_complete.html', {'form_data': form_data})

test_form_wizard_view = TestWizard.as_view(TRANSFER_FORMS)


# ADDRESS LIST VIEW
class AddressListView(ListView):
    pass

#     model = models.Test
#     template_name = 'test_forms/address_list.html'
#     queryset = models.Test.objects.filter(sect1__sect1)

#     def get_context_data(self, **kwargs):
#         context = super(AddressListView, self).get_context_data(**kwargs)
#         return context
