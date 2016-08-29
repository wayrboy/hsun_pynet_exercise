#!/usr/bin/env python

from netmiko import ConnectHandler

rtr2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'secret': '',
    'port': '22',
    'password': '88newclass'
    }

conn1 = ConnectHandler(**rtr2)
conn1.config_mode()

if conn1.check_config_mode():
    print "here you are in config mode"
    print "your prompt is :",
    print conn1.find_prompt()
else:
    print "you are not in config mode"
    print "your prompt is :",
    print conn1.find_prompt()


