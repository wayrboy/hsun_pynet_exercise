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
        checker = vlans[0]['result']['vlans']
        return checker[vlan_id]['name']# for return the name to compare if there's same name when adding
        '''
        if there is a VLAN, there will always be a name for it
        '''
    except (pyeapi.eapilib.CommandError, KeyError):
        return False
        pass

def config_vlan(conn, vlan_id, vlan_name=None):
    '''
    adding a new vlan, or change VLAN's name
    '''
    vlan_commands_set = []
    vlan_command_part1 = 'vlan {}'.format(vlan_id)
    vlan_commands_set.append(vlan_command_part1)
    if vlan_name !=None:
        vlan_command_part2 = ' ' + 'name {}'.format(vlan_name)
        vlan_commands_set.append(vlan_command_part2)
    return conn.config(vlan_commands_set)


def main():
    conn1 = pyeapi.connect_to("pynet-sw1")

    parser = argparse.ArgumentParser(description="Add/Delete VLAN")
    parser.add_argument(
            "--vlan_id",
            help="VLAN number",
            action="store",
            dest="vlan_id",
            type=int
    )
    parser.add_argument(
            "--name",
            help="VLAN name",
            action="store",
            dest="vlan_name",
            type=str
    )
    parser.add_argument(
            "--add",
            help="add the given VLAN",
            action="store_true",
            dest="to_add"
    )
    parser.add_argument(
            "--delete",
            help="delete the given VLAN",
            action="store_true",
            dest="to_delete"
    )

    meta_args = parser.parse_args()
    vlan_id = meta_args.vlan_id
    vlan_name = meta_args.vlan_name
    to_add = meta_args.to_add
    to_delete = meta_args.to_delete

    vlan_existence = vlan_existence_checker(conn1, vlan_id)

    if to_delete:
        print vlan_existence
        if vlan_existence:
            print "Removing this VLAN"
            vlan_command = 'no vlan {}'.format(vlan_id)
            conn1.config(vlan_command)
        else:
            print "Action aborted because there's no such a VLAN"
    if to_add:
        if vlan_existence:
            if vlan_name != None and vlan_existence != vlan_name:
                print "Setting new name for an existed VLAN"
                config_vlan(conn1, vlan_id, vlan_name)
            else:
                print "VLAN exists, no action's required"
        else:
            print "Adding a new VLAN"
            config_vlan(conn1, vlan_id, vlan_name)



if __name__ == "__main__":
    main()
