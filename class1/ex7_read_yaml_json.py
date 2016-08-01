#!/usr/bin/evn python

import json
from pprint import pprint
import yaml

def main():
    '''
    we are going to open the two files created by ex6, and then read them in YAML way and JSON way.
    '''    
    yaml_file = 'yaml_test1.yml'
    json_file = 'json_test1.json'
    
    with open(yaml_file) as stream:
        yaml_list = yaml.load(stream)

    with open(json_file) as stream:
        json_list = json.load(stream)

    print "This is a YAML reading", "\n"
    pprint(yaml_list)
    print "\n"*2, "\n" + "This is a JSON reading" + "\n"
    pprint(json_list)

if __name__ == "__main__":
    main()
