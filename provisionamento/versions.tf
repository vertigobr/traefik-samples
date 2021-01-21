
terraform {
  required_version = ">= 0.12"
}

terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "2.4.0"
    }
  }
}