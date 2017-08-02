from elastictf import libvirttf


def test_resource_attr():
    domain_resource = libvirt.DomainResource(
        test_attr1=1,
        test_attr2='test2',
        test_attr3=False,
    )
    assert domain_resource.test_attr1 == 1
