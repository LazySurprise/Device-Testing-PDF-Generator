# DJANGO imports
from django.conf.urls import url

# LOCAL APP imports
from . import views
from . import forms


urlpatterns = [

    # WIZARD FORM
    url(r'^new_form/$', views.test_form_wizard_view, name='test_form_wizard_view'),

    # WIZARD FORM
    url(r'^new_address_form/$', views.new_test_form_wizard_view, name='new_test_form_wizard_view'),

    # Test Form Complete 
    url(r'^new_form/test_form_complete/$', views.CompleteFormView, name='complete-form'),
    
    # Address list
    url(r'^addresses/$', views.AddressListView.as_view(), name='address-list'),

    # Test list
    url(r'^(?P<slug>[\w-]+)/$', views.TestListView.as_view(), name='test-list'),

    # Test detail
    #url(r'^(?P<slug>[\w-]+)/$', views.TestDetailView.as_view(), name='test-detail'),

    

    

]