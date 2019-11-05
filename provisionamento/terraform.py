#!/usr/bin/env python

import argparse
import json


def get_tfstate_data(statefile):
    try:
        with open(statefile) as state:
            inventory = json.load(state)
            resources = inventory['resources']

        return resources
    except IOError:
        return {}


def parse_tfstate_data(resources):
    instances = []

    attributes = [
#        'ami',
        'image',
#        'availability_zone',
        'region',
#        'instance_type',
#        'private_dns',
#        'private_ip',
#        'public_dns',
#        'public_ip',
#        'tags.Name',
#        'tags.Purpose',
#        'tags.Role',
#        'tags.Type',
#        'tags.Ami'
#        'tags.0',
        'name',
        'ipv4_address'
    ]

    for k in resources:
        if k['type'] == 'digitalocean_droplet': # 'aws_instance':
            for v in k['instances']:
                instance = {}
                instance['group_name'] = k['name']
                for attribute in attributes:
                    if attribute in v['attributes']:
                        instance[attribute] = v['attributes'][attribute]
                    else:
                        instance[attribute] = None

                instances.append(instance)
    return instances


def list(statefile):
    # inventory = {}

    resources = get_tfstate_data(statefile)
    instances = parse_tfstate_data(resources)
    inventory = create_inventory(instances)

    inventory['_meta'] = {}
    inventory['_meta']['hostvars'] = {}
    # hostvars = inventory['_meta']['hostvars']

    return inventory


def create_inventory(instances):
    inventory = {}
    grouping_attrs = [
#        'availability_zone',
#        'tags.Name',
#        'tags.Purpose',
#        'tags.Role',
#        'tags.Type',
#        'tags.Ami'
        'group_name',
#        'tags.0',
        'region'
    ]
    for instance in instances:
        name = instance['ipv4_address'] # public_ip 
        for attr in grouping_attrs:
            if attr in instance:
                group = instance[attr]
                if group:
                    if group in inventory:
                        inventory[group]['hosts'].append(name)
                    else:
                        inventory[group] = {}
                        inventory[group]['hosts'] = [name]

                    inventory[group]['vars'] = {"ansible_user": "root"}
                    #inventory[group]['vars'] = {"ansible_user": "core", "ansible_python_interpreter": "PATH=/home/core/bin:$PATH python"}
                    # role coreos-bootstrap
                    #inventory[group]['roles'] = [ "defunctzombie.coreos-bootstrap" ]
                    #inventory[group]['gather_facts'] = False 
    return inventory


def host(statefile, host):
    # Not supported yet
    # Ansible expects a hash of variables that apply to the host
    # We need to print an empty hash to maintain Ansible compatibility
    # but Ansible doesn't care if there is nothing in it
    empty_dict = {}
    return empty_dict


def main():
    global debug_set

    response = {}

    statefile = 'terraform.tfstate'

    parser = argparse.ArgumentParser(
        description="Return dynamic inventory for Ansible")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--list',
                       action='store_true',
                       default=False,
                       help='return full inventory')
    group.add_argument('--host',
                       action='store',
                       dest='host',
                       type=str,
                       help='return inventory of HOST')
    parser.add_argument('--debug',
                        action='store_true',
                        default=False,
                        help='print debug info while running')

    args = parser.parse_args()

    if args.debug:
        debug_set = args.debug
    else:
        debug_set = False

    if args.list:
        response = list(statefile)

    if args.host:
        response = host(statefile, host)

    if response:
        print(json.JSONEncoder().encode(response))


if __name__ == '__main__':
    main()

