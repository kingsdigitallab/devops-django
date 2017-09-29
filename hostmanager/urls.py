from django.conf.urls import url

from .views.overview import (OverviewIndex)
from .views.servers import (ServersIndex, ServersAdd, ServersSubnetScan)

urlpatterns = [
    url(r'^$', OverviewIndex.as_view(), name='overview'),

    url(r'^servers/$', ServersIndex.as_view(), name='servers'),
    url(r'^servers/add/$', ServersAdd.as_view(), name='servers_add'),
    url(r'^servers/add/subnetscan/$', ServersSubnetScan.as_view(),
        name='servers_add_subnetscan'),


    #    url(r'^project/(?P<project_id>\d+)/$', ProjectView.as_view()),
]
