#!/usr/bin/env python

import pexpect
import time
from ex3_pexpect import create_a_conn

def main():
    '''
    use pexpect to login and enter configure terminal mode
    to issue the command "logging buffer 40961" and then
    verify it by print "show run | inc logging buffer"
    '''

    '''
    one thing is quite interesting, if you set logging buffer to 4096
    then "logging buffer 4096" will not show in "show run | inc logging"
    '''
    ip_addr = '184.105.247.71'
    port  = 22
    username = 'pyclass'
    password = '88newclass'

    conn1 = create_a_conn(ip_addr, port, username, password)
    prompt = conn1.before + conn1.after

    conn1.sendline('terminal length 0')
    conn1.expect(prompt)

    conn1.sendline('config t')
    conn1.expect('#')

    conn1.sendline('logging buffer 40961')
    conn1.expect('#')

    conn1.sendline('end')
    conn1.expect(prompt)

    conn1.sendline('show run | inc logging buffer')
    conn1.expect(prompt)

    print conn1.before

if __name__ == "__main__":
    main()
