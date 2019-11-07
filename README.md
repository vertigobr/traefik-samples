# traefik-samples
Exemplos de Traefik para Meetups

# Provisionamento (Docker em swarm mode)

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

# Provisionamento (Kubernetes)

A pasta `provisionamento` possui um script para criação de cluster kubernetes na Digital Ocean.

```sh
./create-k8s.sh
# para testar
kubectl get nodes
```

# Docker (stand-alone)

A pasta `docker` contém um exemplo de uso do Traefik em um docker engine stand-alone.

```sh
docker-compose up -d
# atribuir IP de manager.vtg para app1.company.com e app2.company.com
curl app1.company.com
curl app2.company.com
docker-compose down
```

# Docker (swarm mode)

A pasta `swarm` contém um exemplo de uso do Traefik em um cluster swarm mode.

```sh
docker stack deploy -c docker-compose.yml webapp
# para testar
curl app1.company.com
curl app2.company.com
# opcional: observar serviços e containers no portainer
docker stack rm webapp
```

# Kubernetes

A pasta `k8s` contém um exemplo de uso do Traefik em um cluster kubernetes.

```sh
kubectl apply -f ./01-traefik/
kubectl apply -f ./02-webapp/
# para testar
curl app3.company.com
```

