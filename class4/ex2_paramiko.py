#!/usr/bin/env python

import paramiko
import time

from ex1_paramiko import create_a_conn, send_a_command
'''
these two functions are just the same as the functions in ex1
'''

def main():
    ip_addr = '184.105.247.71'
    port  = 22
    username = 'pyclass'
    password = '88newclass'

    conn1 = create_a_conn(ip_addr, port, username, password)
    send_a_command(conn1, "conf t")
    send_a_command(conn1, "logging buffered 23333")
    send_a_command(conn1, "end")

    outp = send_a_command(conn1, "sho run | inc logging")

    print outp

if __name__ == "__main__":
    main()
