import snmp_helper
from datetime import datetime
import yaml
# Uptime when running config last changed

ip_addr1 = "184.105.247.70"
ip_addr2 = "184.105.247.71"

port = 161

snmp_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

a_user = (snmp_user, auth_key, encrypt_key)

device1 = (ip_addr1, port)
device2 = (ip_addr2, port)

def get_the_current_value(device, user):
     
    ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    output = snmp_helper.snmp_get_oid_v3(device, user, ccmHistoryRunningLastChanged)
    value = snmp_helper.snmp_extract(output)
    return value


def save_status(filename, value):
    '''
    save the current value of ccmHistoryRunningLastChanged
    '''

    status = []
    status.append({})
    status[-1]['time_stemp'] = str(datetime.now())
    status[-1]['value'] = value
    with open(filename, "a") as stream:
        stream.write(yaml.dump(status, default_flow_style = False))
    print "the following data saved"
    print status

def read_status(filename):
    '''
    read the value of ccmHistoryRunningLastChanged from yaml file
    '''
    try:
        with open(filename, "r") as stream:
            current = yaml.load(stream)
            return current[-1]["value"]
    except IOError:
        return "NULL"
    '''
    do not use print, it will cause the equaty between
    this func and get_the_current_value to be False,
    even when you see it by eye, they look equal to each other
    '''

def no_need_to_save_new(filename, current_value):
    '''
    determin whether to write a new status to yaml file
    '''
    return read_status(filename) == current_value

def config_change_detector(device, user, filename):
    value = get_the_current_value(device, user)

    if no_need_to_save_new(filename, value):
        print "no need to change anything"
    else:
        print "the previous value is " + read_status(filename)
        print "the current value is " + value
        save_status(filename, value) 


config_change_detector(device1, a_user, "device1_status.yml")


def send_email(recipient, subject, message, mail_sender, mail_host, mail_password):

