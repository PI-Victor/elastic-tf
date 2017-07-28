from providers import LibvirtProvider
from resource import Resource


class DomainResource(Resource):
    def __init__(
    self,
    memory=512,
    vcpu=1,
    running='false',
    disk='',
    network_interface='',
    metadata='',
    cloudinit='',
    cpu='',
    autostart='false',
    filesystem=[],
    volume_id='',
    network_name='',
    network_id='',
    addresses='',
    hostname='',
    ):
    self.resource_type = 'libvirt_domain'
    self.memory = memory
    self.vcpu = vcpu
    self.running = running
    self.disk = disk
    self.metadata = metadata
    self.cloudinit = cloudinit
    self.cpu = cpu
    self.autostart = autostart
    self.filesystem = filesystem
    self.volume_id = volume_id
    self.network_interface = network_interface
    self.network_name = network_name
    self.network_id = network_id
    self.addresses = addresses
    self.hostname = hostname


class NetworkResource(Resource):
    def __init__(self, name, domain, mode, addresses):
        self.resource_type = 'libvirt_network'
        self.name = name
        self.domain = domain
        self.mode = mode
        self.addresses = addresses


class CloudInitResource(Resource):
    def __init__(
        self,
        name,
        pool,
        local_hostname,
        ssh_authorized_keys,
        user_data,
    ):
        self.resource_type = 'libvirt_cloudinit'
        self.name = name
        self.pool = pool
        self.local_hostname = local_hostname
        self.ssh_authorized_keys = ssh_authorized_keys
        self.user_data = user_data


class VolumeResource(Resource):
    def __init__(
        self,
        name,
        pool,
        source,
        size,
        base_volume_id,
        base_volume_name,
        base_volume_pool,
    ):
    self.resource_type = 'libvirt_volume'
    self.name = name
    self.pool = pool
    self.source = source
    self.size = size
    self.base_volume_id = base_volume_id
    self.base_volume_name = base_volume_name
    self.base_volume_pool = base_volume_pool
