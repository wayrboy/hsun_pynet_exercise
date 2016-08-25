#!/usr/bin/env python

import snmp_helper
import yaml
import time

ip_addr1 = "184.105.247.70"
port = 161

snmp_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

a_user = (snmp_user, auth_key, encrypt_key)

device1 = (ip_addr1, port)

def get_data(device, user, filename, time_stemp):
    '''
    to get the value of ifInOctets_fa4 and ifOutOctets_fa4
    '''
    ifInOctets_fa4 = '1.3.6.1.2.1.2.2.1.10.5'
    ifOutOctets_fa4 = '1.3.6.1.2.1.2.2.1.16.5'

    data = []
    data.append({})

    data[-1]['time'] = time_stemp

    output = snmp_helper.snmp_get_oid_v3(device, user, ifInOctets_fa4)
    data[-1]['inbound'] = snmp_helper.snmp_extract(output)

    output = snmp_helper.snmp_get_oid_v3(device, user, ifOutOctets_fa4)
    data[-1]['outbound'] = snmp_helper.snmp_extract(output)
    
    with open(filename, "a") as stream:
        stream.write(yaml.dump(data, default_flow_style = False))

for each_five_minute in range(1,13):
    time_stemp = each_five_minute*5
    get_data(device1, a_user, "octets_fa4.yaml", time_stemp)
    print "the time is %d" % time_stemp
    time.sleep(time_stemp)

