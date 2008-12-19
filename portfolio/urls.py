from django.conf.urls.defaults import *
from django.contrib import admin
from views import project_list, project_detail, category_list, skill_detail, skill_list

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(
        regex = r'^project/(?P<slug>[-\w]+)/$',
        view = project_detail,
        name = 'project_detail',

    url(
        regex = r'^category/(?P<slug>[-\w]+)/$',
        view = category_detail,
        name = 'category_detail',
        ),

    url(
        regex = r'^categories/$',
        view = category_list,
        name = 'category_list',
        ),

    url(
        regex = r'^skill/(?P<slug>[-\w]+)/$',
        view = skill_detail,
        name = 'skill_detail',
        ),

    url(
        regex = r'^skills/$',
        view = skill_list,
        name = 'skill_list',
        ),
    

)
