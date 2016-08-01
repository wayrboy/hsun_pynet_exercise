#!/usr/bin/env python
import json
import yaml

def main():
    '''
    This python script will create a list, one of the elements is a dictinary
    wild python, isn't it? with at least two keys. 
    Then we are gonna write this list to a file using both YAML and JSON formats.
    '''

    yaml_file = 'yaml_test1.yml'
    json_file = 'json_test1.json'

    dict_test1 = {
        'ip_addr': '184.105.247.70',
        'snmp_port': '161',
        'ssh_port': '22',
        'username': 'pyclass',
        'password': '88newclass'
    }

    list_test1 = [
        'whatever',
        'winter_is_coming',
        23,
        24,
        'hear me roar'
    ]
    
    dicted_list_test1 = [
        'this is a router',
        'the info is as followings:',
        {'ip_addr': '184.105.247.70',
         'snmp_port': '161',
         'ssh_port': '22',
         'username': 'pyclass',
         'password': '88newclass'},
        233,
        23333,
        'winter is coming',
    ]


    with open(yaml_file, 'w') as stream:
        stream.write(yaml.dump(dicted_list_test1, default_flow_style=False))
    with open(json_file, 'w') as stream:
        json.dump(dicted_list_test1, stream)

if __name__ == "__main__":
    main()
