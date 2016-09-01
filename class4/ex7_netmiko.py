#! /usr/bin/env python

from ex6_netmiko import rtr2
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

def main():
	'''
	Use main() to make the code have a clear structure
	Use netmiko to change the logging buffer on rtr2
	'''
	rtr2['password'] = getpass()
	
	conn1 = ConnectHandler(**rtr2)
	commands = ['logging buffered 22333']
	conn1.send_config_set(commands)

	outp = conn1.send_command("show run | inc logging buffer")

	print "The logging buffer on rtr2 has been changed to following: \n %s" % outp

