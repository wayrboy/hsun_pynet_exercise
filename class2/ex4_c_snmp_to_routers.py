#! /usr/bin/env python

'''
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2)
and prints out both the MIB2 sysName and sysDescr
'''

import snmp_helper

SYS_DESCRT = '1.3.6.1.2.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'

def main():
    ip_addr1 = '184.105.247.70'
    ip_addr2 = '184.105.247.71'

    community_string = 'galileo'

    device1 = (ip_addr1, community_string, 161)
    device2 = (ip_addr2, community_string, 161)

    for each_device in (device1, device2):
        print "*****************"
        for oid in (SYS_NAME, SYS_NAME):
            snmp_data = snmp_helper.snmp_get_oid(each_device, oid=oid)
            output = snmp_helper.snmp_extract(snmp_data)

            print output
        print "*****************"

if __name__ == '__main__':
        main()



