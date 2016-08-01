#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

def main():
# this is a script that can find the crypto maps that are not using certain encryption method
    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
    crypto_map = cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO', childspec=r'AES')
    print "\n", "=="*4, "The crypto maps without AES:", "=="*4, "\n"
    for each_map in crypto_map:
# I have printed so many things to make sure I can get a good data type in while loop
#        print type(each_map.children)
#        print len(each_map.children)
#        print type (each_map.children[child_number])
#        print str(each_map.children[child_number])
        print each_map.text
        child_number = 0
        while child_number < (len(each_map.children)):
            if "transform-set" in str(each_map.children[child_number]):
                print each_map.children[child_number].text, "\n"
                child_number = child_number + 1
            else:
                child_number = child_number + 1


if __name__ == "__main__":
    main()
