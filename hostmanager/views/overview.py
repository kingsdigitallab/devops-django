from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

'''
Our main landing page (aka Overview)
'''


class OverviewIndex(LoginRequiredMixin, TemplateView):
    template_name = 'hostmanager/overview/index.html'

    def get_context_data(self, **kwargs):
        context = super(OverviewIndex, self).get_context_data(**kwargs)
        context['meta_title'] = 'Overview'
        context['status'] = self._get_status()
        return context

    def _get_status(self):
        status = {}
        status['servers'] = {}
        status['services'] = {}

        status['servers']['down'] = 0
        status['servers']['warning'] = 0
        status['services']['down'] = 0
        status['services']['warning'] = 0

        return status
