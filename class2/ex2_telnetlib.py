#! /usr/bin/env python

import sys
import time
import telnetlib
import socket

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def create_a_conn(ip_addr, port, timeout):
    try:
         return telnetlib.Telnet(ip_addr, port, timeout)
    except socket.timeout:
            sys.exit("Connection time out")

def login(conn, username, password=''):
    output = conn.read_until("sername:", TELNET_TIMEOUT)
    conn.write(username + '\n')
    if len(password) > 1:
        output += conn.read_until("ssward:", TELNET_TIMEOUT)
        conn.write(password + '\n')
        return output 
    else:
        return output

def send_command(conn, cmd):
    cmd = cmd.rstrip()
    conn.write(cmd + '\n')
    time.sleep(1)
    return conn.read_very_eager()

def main():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'
    
    conn1 = create_a_conn(ip_addr, TELNET_PORT, TELNET_TIMEOUT)

    output =  login(conn1, username, password)
    time.sleep(1)
    print output
 
    send_command(conn1, 'terminal len 0')
    output = send_command(conn1, 'show ip int br')
    print output
    conn1.close()

if __name__ == '__main__':
    main()

