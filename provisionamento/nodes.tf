
variable "do_token" {}

variable "ssh_keys" {
  default = []
}

variable "do_image" {
  default = "centos-7-x64"
}

variable "qtdman" {
  default = 1
}

variable "qtdwor" {
  default = 2
}

# Configure the DigitalOcean Provider
provider "digitalocean" {
  token = var.do_token
}

# Create swarm manager and workers
resource "digitalocean_droplet" "managers" {
  count    = var.qtdman
  image    = var.do_image
  name     = "manager${count.index}"
  region   = "nyc3"
  size     = "s-1vcpu-1gb"
  ssh_keys = var.ssh_keys
  private_networking = true
}

resource "digitalocean_droplet" "workers" {
  count    = var.qtdwor
  image    = var.do_image
  name     = "worker${count.index}"
  region   = "nyc3"
  size     = "s-1vcpu-1gb"
  ssh_keys = var.ssh_keys
  private_networking = true
}

output "manager_ip" {
  value = digitalocean_droplet.managers[0].ipv4_address
}

