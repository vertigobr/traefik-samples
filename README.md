# traefik-samples
Exemplos de Traefik para Meetups

# Provisionamento (Docker em swarm mode)

A pasta `provisionamento` contém o terraform para criação das VMs da Digital Ocean e a role ansible para configurar Swarm Mode com socket seguro.

```sh
terraform init
terraform apply
# mostra inventário dinâmico
python terraform.py --debug --list | jq
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
# abrir http://manager.vtg:9000 no browser
```

# Docker (stand-alone)

A pasta `docker` contém um exemplo de uso do Traefik em um docker engine stand-alone.

```sh
docker-compose up -d
# atribuir IP de manager.vtg para app1.company.com e app2.company.com
curl app1.company.com
curl app2.company.com
# mostrar apps no portainer em http://manager.vtg:9000/#/containers
# mostrar rotas no traefik em http://manager.vtg:8080/dashboard/#/http/routers
docker-compose down
```

# Docker (swarm mode)

A pasta `swarm` contém um exemplo de uso do Traefik em um cluster swarm mode.

```sh
docker stack deploy -c docker-compose.yml webapp
# para testar
curl app1.company.com
curl app2.company.com
curl app1.company.com # repetir e mostrar IP variando (scale=2)
# opcional: observar serviços e containers no portainer
# mostrar apps no portainer em http://manager.vtg:9000/#/containers (cluster visualizer)
# mostrar rotas no traefik em http://manager.vtg:8080/dashboard/#/http/routers
docker stack rm webapp
```

# Provisionamento (Kubernetes)

A pasta `provisionamento` possui um script para criação de cluster kubernetes na Digital Ocean.

```sh
./create-k8s.sh
# para testar
kubectl get nodes
```

# Kubernetes

A pasta `k8s` contém um exemplo de uso do Traefik em um cluster kubernetes.

```sh
kubectl apply -f ./01-traefik/
# aguardar IP externo do load balancer do traefik
kubectl get svc -w
# atribuir IP externo para cluster.vtg no /etc/hosts
# abrir traefik dashboard em http://cluster.vtg/dashboard/#/
kubectl apply -f ./02-webapp/
# para testar
curl app3.company.com
```

