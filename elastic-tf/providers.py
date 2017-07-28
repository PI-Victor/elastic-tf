from abc import ABCMeta


class Provider(metaclass=ABCMeta):
    '''Provider is an abstract class that all
    providers should implement
    '''


class LibvirtProvider(Provider):
    '''LibvirtProvider contains details needed
    for the functionality of the libvirt plugin.
    '''
    def __init__(self, URI='qemu:///system'):
        self.name = 'libvirt'
        self.URI = URI

    def __str__(self):
        return '''"provider" "%s" {
    uri = "%s"
}''' % (self.name, self.URI)
