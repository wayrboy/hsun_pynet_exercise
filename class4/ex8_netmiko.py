#! /usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

rtr1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'secret': '',
    'port': '22',
    'password': '88newclass',
    }


rtr2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'secret': '',
    'port': '22',
    'password': '88newclass',
    }


def get_name_of_obj(obj, except_word = ""):
    for name, item in globals().items():
        if item == obj and name != except_word:
            return name


def main():

    for each_item in [rtr1, rtr2]:
        
        conn1 = ConnectHandler(**each_item)
        conn1.send_config_from_file(config_file = 'config_snippet.txt')

        outp = conn1.send_command("show run | inc logging")
        hostname = get_name_of_obj(each_item, "each_item")
        print "Logging buffer size and logging console info on %s :" % hostname
        print outp + "\n" + "***********************"

if __name__ == "__main__":
    main()
