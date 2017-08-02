from elastictf import providers

def test_libvirt_provider():
    new_libvirt = providers.LibvirtProvider()
    assert new_libvirt.URI == 'qemu:///system'
    assert new_libvirt.name == 'libvirt'
