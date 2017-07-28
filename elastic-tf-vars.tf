variable "image" {
  default = "https://download.fedoraproject.org/pub/fedora/linux/releases/26/CloudImages/x86_64/images/Fedora-Cloud-Base-26-1.5.x86_64.qcow2"
}

variable "ssh_authorized_key" {
  default = <<EOF
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQChT9Yk7pKbrRyRLga1RyESyluYEs9zJ57h5OX+r5sVkoF/4nf9UBtanYTKL8DdyM5wS7GQMyJ2rYGf+i53X9ePah2/2j1LXDCnKeuFhdzwchAt7EBcR1eeWHnKSm/pZgfVvVP5ndxpNEWo39qyAnTn+GzmCeIh1Kb6yeDKxxJTOU96iG8tPNeboo+y8bS0xZyeEUj/3EtqSTMBn2Jbwqo5sPzsyNsfQ0ZVugmvUIZJu1WYUrT3BGqjlWQn8V9xZuLuRUUHjGsD32x/O9r+Vbn6Wdpxz9bcAafni4+/he1qX8CDuNfPy9OmwR9rEueXiS2dwe5q34OapXQBvyn1Oke3 vpalade@k8senv
  EOF
}

variable "user_data" {
  default = <<EOF
    groups:
      - ubuntu: [foo,bar]
      - cloud-users

    users:
      - default
      - name: foobar
        gecos: Foo B. Bar
        plain_text_passwd: test
        primary-group: foobar
        groups: users wheel
        selinux-user: staff_u
        expiredate: 2012-09-01
        ssh-import-id: foobar
        lock_passwd: false
  EOF
}
