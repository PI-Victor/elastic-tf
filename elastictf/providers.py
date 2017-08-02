from abc import ABCMeta


class ResourceDefinition():
    def __init__(self, resource_type, resource_name, **resource_params):
        pass
        
    def __repr__(self):
        pass


class Provider(metaclass=ABCMeta):
    '''Provider is an abstract class that all providers should implement.
    '''
    pass


class LibvirtProvider(Provider):
    '''LibvirtProvider contains details needed for the functionality of the
    libvirt plugin.
    '''
    def __init__(self, URI='qemu:///system'):
        self.name = 'libvirt'
        self.URI = URI

    def __str__(self):
        return '''"provider" "%s" {
    uri = "%s"
}''' % (self.name, self.URI)
