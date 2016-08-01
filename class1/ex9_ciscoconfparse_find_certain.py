#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

'''
the following is a faild trial, I wanted to put a %s to find_objects(r"^string")

#def print_crypto_map_with_certain(conf_file, parent, child_element, object_crypto_map):
def print_crypto_map_with_certain(conf_file, parent): 
    cisco_cfg = CiscoConfParse(confi_file)
    cisco_snippet = cisco_cfg.find_objects(r"^%s" % parent)
    print cisco_snippet

target_file = "cisco_ipsec.txt"
parent_string = "crypto map CRYPTO"
#print_crypto_map_with_certain(target_file, parent_string)
'''

def main():
    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
    crypto_map = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec=r'pfs group2')
    
    print "\n the crypto maps with pfs group2 :", "\n"
    for each_map in crypto_map:
        print each_map.text

if __name__ == "__main__":
    main()
