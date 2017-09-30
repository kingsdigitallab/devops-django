from django import template
from hostmanager.models import Server

register = template.Library()

# Gets a list of servers


@register.simple_tag(takes_context=True)
def navigation_server_list(context):
    servers = Server.objects.all().order_by('hostname')
    return servers
