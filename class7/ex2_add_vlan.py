#! /usr/bin/env python

import pyeapi
import argparse

def vlan_existence_checker(conn, vlan_id):
    '''
    checked if this vlan is existed on this switch
    '''
    vlan_id = str(vlan_id)
    # make vlan_id to string

    cmd = 'show vlan id {}'.format(vlan_id)
    
    try:
        vlans = conn.enable(cmd)
        checker = vlans[0]['result']
        return checker[vlan_id]['name']
    except (pyeapi.eapilib.CommandError, KeyError):
        print "VLAN not found"
        pass

def add_vlan(conn, vlan_id, vlan_name=None):
    '''
    adding a new vlan
    '''
    vlan_command_part1 = 'vlan {}'.format(vlan_id)
    if vlan_name !=None:
        vlan_command = vlan_command_part1 + ' ' + 'name {}'.format(vlan_name)
        print vlan_command
        print type(vlan_command)


def main():
    conn1 = pyeapi.connect_to("pynet-sw1")
    vlan_existence_checker(conn1, 150)
    add_vlan(conn1, 150, 'test')

if __name__ == "__main__":
    main()
