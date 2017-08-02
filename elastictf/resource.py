from abc import ABCMeta

class Resource(metaclass=ABCMeta):
    '''Resource is an abstract class from which all the terraform resources
    derive from.
    The parameter documentation for the derived classes can be found at https://github.com/dmacvicar/terraform-provider-libvirt/blob/master/docs/providers/libvirt/index.html.markdown
    '''
    def __init__(self, **kwargs):
        '''Instead of passing a really large number of parameters that might
        change, we add them dinamycally at runtime.
        '''
        # NOTE: This could clash with the class internals, need to do some error
        # handling and validation.
        for (k, v) in kwargs.iteritems():
            setattr(self, k, v)
