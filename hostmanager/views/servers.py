from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

'''
Index page for the server list
'''


class ServersIndex(LoginRequiredMixin, TemplateView):
    template_name = 'hostmanager/servers/index.html'

    def get_context_data(self, **kwargs):
        context = super(ServersIndex, self).get_context_data(**kwargs)
        context['meta_title'] = 'Servers'

        return context


'''
Add server page
'''


class ServersAdd(LoginRequiredMixin, TemplateView):
    template_name = 'hostmanager/servers/add.html'

    def get_context_data(self, **kwargs):
        context = super(ServersAdd, self).get_context_data(**kwargs)
        context['meta_title'] = 'Add a Server'
        return context


'''
Scan a subnet for new servers
'''


class ServersSubnetScan(LoginRequiredMixin, TemplateView):
    template_name = 'hostmanager/servers/add/subnetscan.html'

    def get_context_data(self, **kwargs):
        context = super(ServersSubnetScan, self).get_context_data(**kwargs)
        context['meta_title'] = 'Scan for Servers'
        return context
