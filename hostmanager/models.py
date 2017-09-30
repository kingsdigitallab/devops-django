from django.db import models
from django.conf import settings

import os

from .utils.files import clean_path

# Network level modules


class NetworkDomain(models.Model):
    fqdn = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='Domain Name')
    name = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name='Optional Friendly Name')
    description = models.TextField(
        blank=True, null=True, verbose_name='Optional Description')

    class Meta:
        verbose_name = 'Domain Name'
        verbose_name_plural = 'Domain Names'

    def __str__(self):
        if self.name:
            return '{} ({})'.format(self.fqdn, self.name)
        else:
            return self.fqdn

    def __unicode__(self):
        return self.__str__()

    @classmethod
    def create(cls, fqdn):
        obj = cls(fqdn=fqdn)
        return obj

# OS Level Models

# E.g. x86_84


class OperatingSystemArch(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='OS Arch Name')

    class Meta:
        verbose_name = 'Operating System Architecture'
        verbose_name_plural = 'Operating System Architectures'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    @classmethod
    def create(cls, name):
        obj = cls(name=name)
        return obj


# E.g. Freebsd/Linux
class OperatingSystemPlatform(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='OS Type Name')

    class Meta:
        verbose_name = 'Operating System Platform'
        verbose_name_plural = 'Operating System Platforms'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    @classmethod
    def create(cls, name):
        obj = cls(name=name)
        return obj


# E.g. Debian/Ubuntu
class OperatingSystemDistribution(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='OS Distribution')
    platform = models.ForeignKey(OperatingSystemPlatform)

    class Meta:
        verbose_name = 'Operating System Distribution'
        verbose_name_plural = 'Operating System Distributions'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    @classmethod
    def create(cls, name):
        obj = cls(name=name)
        return obj


# E.g. Linux, Windows
class OperatingSystem(models.Model):
    arch = models.ForeignKey(
        OperatingSystemArch, verbose_name='Architecture', blank=False)
    distribution = models.ForeignKey(
        OperatingSystemDistribution, blank=False, verbose_name='Distribution')
    version = models.CharField(
        max_length=255, blank=False, null=False, verbose_name='Version Name')

    class Meta:
        verbose_name = 'Operating System'
        verbose_name_plural = 'Operating Systems'

    def __str__(self):
        return '{} {} ({})'.format(self.distribution.name, self.version,
                                   self.arch)

    def __unicode__(self):
        return self.__str__()

    def get_snippet_path(self):
        return os.path.join(settings.SNIPPET_PATH,
                            clean_path(self.distribution.name),
                            self.version, self.arch.name)

    @classmethod
    def create(cls, name):
        obj = cls(name=name)
        return obj


# Server Models
class ServerCategory(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='Name')

    class Meta:
        verbose_name = 'Server Category'
        verbose_name_plural = 'Server Categories'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    @classmethod
    def create(cls, name):
        obj = cls(name=name)
        return obj


# Server Models
class Server(models.Model):
    name = models.CharField(max_length=255, blank=True,
                            null=True, verbose_name='Optional Friendly Name')
    hostname = models.CharField(
        max_length=255, blank=False, null=False, verbose_name='Hostname')
    domain = models.ForeignKey(
        NetworkDomain, blank=False, null=False, verbose_name='Domain')
    ip = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='IP Address',
        help_text='Will be automatically\
        populated if the domain is registered.')
    category = models.ForeignKey(
        ServerCategory, blank=True, null=True,
        verbose_name='Server Category')
    description = models.TextField(
        blank=True, null=True, verbose_name='Optional Description')

    operating_system = models.ForeignKey(
        OperatingSystem, blank=False, null=False,
        verbose_name="Operating System")

    class Meta:
        verbose_name = 'Server'
        verbose_name_plural = 'Servers'

    def __str__(self):
        if self.name:
            return '{}.{} ({})'.format(self.hostname,
                                       self.domain.fqdn, self.name)
        else:
            return self.hostname

    def __unicode__(self):
        return self.__str__()

    def get_fqdn(self):
        return '{}.{}'.format(self.hostname, self.domain.fqdn)

    @classmethod
    def create(cls, hostname):
        obj = cls(hostname=hostname)
        return obj
