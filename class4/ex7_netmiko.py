#! /usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

rtr2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'secret': '',
    'port': '22',
    }

rtr2['password'] = getpass()
def main():
	'''
	Use main() to make the code have a clear structure
	Use netmiko to change the logging buffer on rtr2
	'''
	conn1 = ConnectHandler(**rtr2)
	commands = ['logging buffered 22333'] 
	conn1.send_config_set(commands)

	outp = conn1.send_command("show run | inc logging buffer")

	print "The logging buffer on rtr2 has been changed to following: \n %s" % outp

if __name__ == "__main__":
    main()
