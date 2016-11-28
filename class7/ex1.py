#! /usr/bin/env python

import pyeapi
from pprint import pprint as pp

def main():
    '''
    grab "show interface" from switch side
    '''

    conn1 = pyeapi.connect_to("pynet-sw1")

    interfaces = conn1.enable("show interfaces")
    interfaces = interfaces[0]['result']

    interfaces = interfaces['interfaces']


    data = {}
    for interface, meta in interfaces.items():
        interfaceCounters = meta.get('interfaceCounters', {})
        data[interface] = (interfaceCounters.get('inOctets'), interfaceCounters.get('outOctets'))


    '''
    print out formatted data, I don't know how to print it beautifully, so I referred the solution of teacher
    '''
    print "\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets")
    for intf, octets in data.items():
        print "{:20} {:<20} {:<20}".format(intf, octets[0], octets[1])


if __name__ == '__main__':
    main()
