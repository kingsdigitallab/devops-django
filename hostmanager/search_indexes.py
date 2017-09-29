from haystack import indexes

from .models import Server


class ServerIndex(indexes.SearchIndex, indexes.Indexable):
    name = indexes.CharField(model_attr='name')
    hostname = indexes.CharField(model_attr='hostname')
    ip = indexes.CharField(model_attr='ip')
    category = indexes.FacetCharField(model_attr='category__name')
    description = indexes.CharField(model_attr='description')
    fqdn = indexes.CharField()

    text = indexes.CharField(document=True)

    operating_system = indexes.FacetCharField(model_attr='operating_system')
    distribution = indexes.FacetCharField(
        model_attr='operating_system__distribution')
    platform = indexes.FacetCharField(model_attr='operating_system__platform')

    def get_model(self):
        return Server

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare_fqdn(self, object):
        return '{}.{}'.format(object.hostname, object.domain.fqdn)
