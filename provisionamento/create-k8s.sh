#!/bin/sh
echo "Lista de clusters:"
doctl kubernetes cluster list
echo "Criando novo cluster:"
doctl kubernetes cluster create meetup --region nyc3 --node-pool "name=mainpool;size=s-2vcpu-4gb;count=3"
echo "Exportando kubeconfig:"
doctl kubernetes cluster kubeconfig save meetup

