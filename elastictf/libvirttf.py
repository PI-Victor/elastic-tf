from providers import LibvirtProvider
from resource import Resource


class DomainResource(Resource):
    def __init__(self, **kwargs):
        super(DomainResource, self).__init__(**kwargs)
        self._resource_name = 'libvirt_domain'
        self._provider_resources = [
            'libvirt_network',
            'libvirt_volume',
            'libvirt_cloudinit',
        ]

    def set_cloudinit(self):
        pass

    def set_disk(self):
        pass

    def set_network(self):
        pass

    def create_interop(self):
        pass

class NetworkResource(Resource):
    def __init__(self, **kwargs):
        super(DomainResource, self).__init__(**kwargs)
        self._resource_name = 'libvirt_network'
        self._resource_type = 'network'
        self.id = None


class CloudInitResource(Resource):
    def __init__(self, **kwargs):
        super(DomainResource, self).__init__(**kwargs)
        self._resource_name = 'libvirt_cloudinit'
        self._resource_type = 'cloudinit'
        self.id = None


class VolumeResource(Resource):
    def __init__(self, **kwargs):
        super(DomainResource, self).__init__(**kwargs)
        self._resource_name = 'libvirt_volume'
        self._resource_type = 'volume'
        self.id = None
