from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from app import views

urlpatterns = patterns('',

                       url(r'^$', views.home, name='home'),
                       url(r'^home/$', views.home, name='home'),
                       url(r'^aboutus/$', views.aboutus, name='aboutus'),
                       url(r'^login/$', views.login_page, name='login'),
                       url(r'^organizationLogin/$',
                           views.organization_login_page, name='login'),
                       url(r'^organizationLoginRequest/$',
                           views.organization_login_request, name='login'),
                       url(r'^login2/$', views.login2, name='login'),
                       url(r'^signup/$', views.signup, name='signup'),
                       url(r'^orgsignup2/$', views.OrgSignUpRequest,
                           name='OrgSignUp'),
                       url(r'^volunteam/$', views.volunteam, name='volunteam'),
                       url(r'^signup2/$', views.signupRequest, name='signup'),
                       url(r'^showUsers/$', views.showUsers,
                           name='Show users'),
                       url(r'^events/$', views.events, name='Events'),
                       url(r'^addEvent/$', views.addEvent, name='AddEvent'),
                       url(r'^logout/$', views.logoutrequest, name='LogOut'),
                       url(r'^OrgSignUp/$', views.OrgSignUp, name='OrgSignUp'),
                       url(r'^managment/$', views.managment, name='managment'),
                       url(r'^managment2/$', views.managment2,
                           name='managment2'),
                       url(r'^photos/$', views.photos, name='photos'),
                       )
