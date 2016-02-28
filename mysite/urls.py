from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import patterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
               
               
    url(r'^$', 'polls.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),

               
    # user auth urls
    url(r'^accounts/login/$',  'polls.views.login'),
    url(r'^accounts/auth/$',  'polls.views.auth_view'),
    url(r'^accounts/logout/$', 'polls.views.logout'),
    url(r'^accounts/loggedin/$', 'polls.views.loggedin'),
    url(r'^accounts/invalid/$', 'polls.views.invalid_login'),
    url(r'^accounts/register/$', 'polls.views.register_user'),
    url(r'^accounts/register_success/$', 'polls.views.register_success'),
    url(r'^accounts/admin/$', 'polls.views.admin_ui'),
    
    # report
    url(r'^reports/new/$',  'polls.views.new_report'),
    url(r'^reports/list/$',  'polls.views.user_report'),
    url(r'^reports/detail/(?P<id>\d+)/$', 'polls.views.report_details'),
    url(r'^reports/delete/(?P<id>\d+)/$','polls.views.delete'),
    url(r'^reports/all/$','polls.views.report_all'),
    url(r'^reports/edit/(?P<id>\d+)/$', 'polls.views.edit_report'),
               
    # folder
    url(r'^folder/new/$', 'polls.views.new_folder'),
    
    #search
    url(r'^search-form/$', 'polls.views.search_form'),
    url(r'^search/$', 'polls.views.search'),
               
    
    #group
    url(r'^group/$', 'polls.views.group'),
               
    #json
    url(r'^api/reports/$','polls.views.ajax_get_data'),
    url(r'^api/users/$','polls.views.ajax_get_user'),
    url(r'^upload/(?P<path>.*)$','django.views.static.serve', {'document_root': '/Users/trinity/Documents/work/cs3240/project/mysite/upload/'}),
               
    #admin_ui
    url(r'^group/new/$', 'polls.views.new_group'),
    
        
    #extra
    url(r'^why/$','polls.views.why'),
    url(r'^sap/$', 'polls.views.sap')
]


