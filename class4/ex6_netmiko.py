#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

rtr1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'secret': '',
    'port': '22',
    }

rtr2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'secret': '',
    'port': '22',
    }

srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'port': 22,
    }

password = getpass()
for each_device in [rtr1, rtr2, srx]:
    each_device['password'] = password

def get_name_of_obj(obj, except_word = ""):
    '''
    Python doesn't even have a BIF to show the name of object?
    '''
    for name, item in globals().items():
        if item == obj and name != except_word:
            return name


for each_device in [rtr1, rtr2, srx]:
    '''
    print ARP on each_device
    '''
    conn = ConnectHandler(**each_device)
    print "ARP table on %s :" % get_name_of_obj(each_device, "each_device")
    arp = conn.send_command("show arp")
    print arp
    print "*********************\n"
