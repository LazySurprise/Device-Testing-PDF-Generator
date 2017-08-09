# DJANGO imports
from django.conf.urls import url

# LOCAL APP imports
from . import views
from . import forms

urlpatterns = [
    url(r'^section1/$', views.Sect1View.as_view(), name='sect1'),
    url(r'^section2/$', views.Sect2View.as_view(), name='sect2'),
    
    # TEMPORARY pdf 
    url(r'^pdf/$', views.PDFView, name='pdfview'),

    # WIZARD FORM
    url(r'^new_form/$', views.TestWizard.as_view([forms.Sect1Form, forms.Sect2Form]), name='test_form_wizard_view'),

]