# traefik-samples
Exemplos de Traefik para Meetups

# Provisionamento

A pasta `provisionamento` contém o terraform para criação das VMs da Digital Ocean e a role ansible para configurar Swarm Mode com socket seguro.

```sh
terraform init
terraform apply
ansible-playbook -i terraform.py install.yml
source env.sh
# para testar
docker node ls
```


