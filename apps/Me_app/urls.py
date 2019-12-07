from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^myschool$', views.myschool),
    url(r'^certifyschools$', views.certifyschools),
    url(r'^whycertificate$', views.whycertificate),
    url(r'^certification$', views.certification),
    url(r'^profilepage$',views.sign_in),
    url(r'^Blog$',views.blog),
    url(r'^ContactUs$',views.contactus),
    url(r'^faqs$',views.faqs),
    url(r'^feedback$',views.feedback),
    ]