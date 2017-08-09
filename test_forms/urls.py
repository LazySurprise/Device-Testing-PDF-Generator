# DJANGO imports
from django.conf.urls import url

# LOCAL APP imports
from . import views
from . import forms

urlpatterns = [
    url(r'^section1/$', views.Sect1View.as_view(), name='sect1'),
    url(r'^section2/$', views.Sect2View.as_view(), name='sect2'),
    
    # Address list
    url(r'^addresses/$', views.AddressListView.as_view(), name='address-list'),

    # WIZARD FORM
    url(r'^new_form/$', views.TestWizard.as_view([forms.CompleteTestForm, forms.Sect1Form, forms.Sect2Form]), name='test_form_wizard_view'),

    # Test Form Complete 
    url(r'^test_form_complete/$', views.TestFormCompleteView, name='test-form-complete'),

]