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

    # Address detail
    url(r'^(?P<slug>[\w-]+)/$', views.AddressDetailView.as_view(), name='address-detail'),

    # WIZARD FORM
    url(r'^new_form/$', views.test_form_wizard_view, name='test_form_wizard_view'),

    # Test Form Complete 
    url(r'^new_form/test_form_complete/$', views.TestFormCompleteView, name='test-form-complete'),

]