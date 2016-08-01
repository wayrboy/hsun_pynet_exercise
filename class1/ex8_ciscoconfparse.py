#!/usr/bin/evn python

from ciscoconfparse import CiscoConfParse
from pprint import pprint

# set the function to print item.text
def print_crypto_map(obj_crypto_map):
    for map in obj_crypto_map:
        print map.text
    print "\n"

def print_map_children(obj_crypto_map):
    print "=="*4, "%d crypto map(s)" %len(obj_crypto_map), "=="*4, "\n"
    for map in obj_crypto_map:
        print map.text
        for child in  map.children:
            print child.text
        print "\n"


cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
#print cisco_cfg

crypto_map1 = cisco_cfg.find_objects(r"^crypto map CRYPTO")
#pprint (crypto_map1)

print_crypto_map(crypto_map1)
print_map_children(crypto_map1)
