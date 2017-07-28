provider "libvirt" {
  uri = "qemu:///system"
}

resource "libvirt_volume" "fedora_volume" {
  name   = "fedora_volume"
  source = "${var.image}"
}

resource "libvirt_cloudinit" "fedora_cloudinit" {
  name               = "libvirt_cloudinit"
  local_hostname     = "fedora_spinoff"
  ssh_authorized_key = "${var.ssh_authorized_key}"
  user_data          = "${var.user_data}"
}

resource "libvirt_domain" "node1" {
  name = "node1"

  disk {
    volume_id = "${libvirt_volume.fedora_volume.id}"
  }

  cloudinit = "${libvirt_cloudinit.fedora_cloudinit.id}"
}
