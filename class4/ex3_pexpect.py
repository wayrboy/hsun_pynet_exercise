#!/usr/bin/env python

import pexpect 
import time

def create_a_conn(ip_addr, port, username, password):
    '''
    return a connection
    '''
    conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    conn.timeout = 3
    conn.expect('ssword:')
    conn.sendline(password)
    conn.expect('#')
    conn.send('\n')
    time.sleep(1)
    conn.expect('#')

    return conn

def main():
    '''
    use pexpect to "sho ip int br"
    '''

    ip_addr = '184.105.247.71'
    port  = 22
    username = 'pyclass'
    password = '88newclass'


    conn1 = create_a_conn(ip_addr, port, username, password)
    prompt = conn1.before + conn1.after

    conn1.sendline('terminal length 0')
    conn1.expect(prompt)

    conn1.sendline('show ip int br')
    conn1.expect(prompt)

    print conn1.before


if __name__ == "__main__":
    main()
