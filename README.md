# traefik-samples
Exemplos de Traefik para Meetups

# Provisionamento

A pasta `provisionamento` contém o terraform para criação das VMs da Digital Ocean e a role ansible para configurar Swarm Mode com socket seguro.

```sh
terraform init
terraform apply
# atribui IP para manager.vtg no /etc/hosts
ansible -i terraform.py -m ping all
ansible-playbook -i terraform.py install.yml
source env.sh
# para testar
docker node ls
```

Opcional: implantar o `portainer` e abrir um túnel local para acesso:

```sh
docker stack deploy -c portainer-service.yml portainer
ssh -L 9000:localhost:9000 root@manager.vtg
```


# Docker (stand-alone)

A pasta `docker` contém um exemplo de uso do Traefik em um docker engine stand-alone.

```sh

```

