#!/usr/bin/env python

import snmp_helper
import yaml
import time
import sys
import pygal
import os


ip_addr1 = "184.105.247.70"
port = 161

snmp_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

a_user = (snmp_user, auth_key, encrypt_key)

device1 = (ip_addr1, port)

ifInOctets_fa4 = '1.3.6.1.2.1.2.2.1.10.5'
ifOutOctets_fa4 = '1.3.6.1.2.1.2.2.1.16.5'
ifInUcastPkts_fa4 = '1.3.6.1.2.1.2.2.1.11.5'
ifOutUcastPkts_fa4 = '1.3.6.1.2.1.2.2.1.17.5'


def empty_file(filename):
    with open(filename, "w"): pass

def get_data(device, user, filename, time_stemp, inboundOID, outboundOID):
    '''
    to get the value of ifInOctets_fa4 and ifOutOctets_fa4
    '''

    data = []
    data.append({})

    data[-1]['time'] = time_stemp

    output = snmp_helper.snmp_get_oid_v3(device, user, inboundOID)
    data[-1]['inbound'] = snmp_helper.snmp_extract(output)

    output = snmp_helper.snmp_get_oid_v3(device, user, outboundOID)
    data[-1]['outbound'] = snmp_helper.snmp_extract(output)
    
    with open(filename, "a") as stream:
        stream.write(yaml.dump(data, default_flow_style = False))

def get_graph(filename, graphfile):
    '''
    get a graph from yaml file
    '''
    chart = pygal.Line()
    
    chart.x_labels = get_data_from_yaml(filename, "time")  
    inbound = get_data_from_yaml(filename, "inbound")
    outbound = get_data_from_yaml(filename, "outbound")

    chart.add('InOctets', inbound)
    chart.add('OutOctets', outbound)

    chart.render_to_file(graphfile)




def get_data_from_yaml(filename, key):
    '''
    get data from yaml file, reform the data into list
    the x-label will have 12 5-minutes
    '''
    with open(filename, "r") as stream:
        data = yaml.load(stream)

    listValue = []

    for each_item in data:
        listValue.append(int(each_item[key]))

    if key == "time":

        del listValue[0]

    elif key == "inbound" or key =="outbound":
        newlist = []
        for i in range (1, len(listValue)):
            newlist.append(listValue[i] - listValue[i-1])
        listValue = newlist

    stream.close()
    return listValue

def get_graph_from_OIDs(device, inboundOID, outboundOID, svgfilename):
    '''
    get data from OIDs, then make them into yaml file, then read yaml to make svg
    yaml file will be deleted after svg created
    '''
    try:
        empty_file("something.yaml")
    except:
        pass

    if inboundOID == ifInOctets_fa4:
        progress = "in/out octets"
    elif inboundOID == ifInUcastPkts_fa4:
        progress = "in/out packets"
    else:
        print "parameter error"
        sys.exit()

    print "creating svg for %s" % progress
    for each_five_minute in range(0,13):
        time_stemp = each_five_minute*5
        get_data(device1, a_user, "something.yaml", time_stemp, inboundOID, outboundOID)
        time.sleep(5)
        print "the timestemp is %d" % time_stemp

    get_graph("something.yaml", svgfilename)
    os.remove("something.yaml")
    print "svg for %s is created" % progress
    print "the filename is %s" % svgfilename
    print "*******************************"


get_graph_from_OIDs(device1, ifInOctets_fa4, ifOutOctets_fa4, "octets_fa4.svg")
get_graph_from_OIDs(device1, ifInUcastPkts_fa4, ifOutUcastPkts_fa4, "pkts_fa4.svg")
