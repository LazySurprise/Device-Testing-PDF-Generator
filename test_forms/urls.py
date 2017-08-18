# DJANGO imports
from django.conf.urls import url

# LOCAL APP imports
from . import views



urlpatterns = [

    # WIZARD FORM FOR NEW ADDRESS
    url(r'^new_address_form/$', views.IndependentCustomerAddressView.as_view(), name='new-address'),

    # view for creating foreign key relationship
    url(r'^(?P<slug>[\w-]+)/address_check/$', views.InspectionFormView.as_view(), name='address-check'),

    # New form from new address page
    url(r'^(?P<slug>[\w-]+)/new_address_inspection/$', views.new_test_form_wizard_view, name='new-address-form'),

    # Test Form Complete 
    url(r'^new_form/test_form_complete/$', views.CompleteFormView, name='complete-form'),
    
    # Address list
    url(r'^addresses/$', views.AddressListView.as_view(), name='address-list'),

    # Test list
    url(r'^(?P<slug>[\w-]+)/$', views.TestListView.as_view(), name='test-list'),

    # Test list
    url(r'^(?P<slug>[\w-]+)/new_form/$', views.test_form_wizard_view, name='test_form_wizard_view'),
   

]