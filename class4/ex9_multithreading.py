#!/usr/bin/env python

import threading
from netmiko import ConnectHandler
from getpass import getpass
import sys
import time

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

def printARP(device):
    '''
    print the ARP table on this device
    '''
    conn = ConnectHandler(**device)
    #sys.stdout.flush()

    arp = conn.send_command("show arp")
    time.sleep(1)
    outp =  ("ARP table on %s :" % get_name_of_obj(device, "each_device")+"\n")
    # use find_prompt() to determin the output of threads are not messed up
    outp +=  (conn.find_prompt()+"\n")
    outp +=  (arp+"\n")
    outp += "*********************\n"
    sys.stdout.write(outp)

class myThread(threading.Thread):
    def __init__(self,  device):
        threading.Thread.__init__(self)
        self.device = device
    def run(self):
        threadLock1 = threading.Lock()
        threadLock1.acquire()
        printARP(self.device)
        threadLock1.release()

def main():
    '''
    using threading here
    '''
    thread1 = threading.Thread(target=printARP, args=[rtr1])
    thread2 = threading.Thread(target=printARP, args=[rtr2])
    thread3 = threading.Thread(target=printARP, args=[srx])


    '''
    thread1 = myThread(rtr1)
    thread2 = myThread(rtr2)
    thread3 = myThread(srx)
    '''

    thread1.start()
    thread2.start()
    thread3.start()
      
    threads = []
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)


    for t in threads:
        t.join()

    print "All done"
if __name__ == "__main__":
    main()
