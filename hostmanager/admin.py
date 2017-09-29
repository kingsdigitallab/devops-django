from django.contrib import admin

from .models import (NetworkDomain,
                     OperatingSystemArch, OperatingSystemDistribution,
                     OperatingSystemPlatform, OperatingSystem,
                     ServerCategory, Server)

# For development, not needed in production
admin.site.register(NetworkDomain)
admin.site.register(OperatingSystemArch)
admin.site.register(OperatingSystemDistribution)
admin.site.register(OperatingSystemPlatform)
admin.site.register(OperatingSystem)
admin.site.register(ServerCategory)
admin.site.register(Server)
