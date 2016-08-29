#!/usr/bin/env python

import paramiko
import time


def create_a_conn(ip_addr, port, username, password):
    '''
    creat a conn to router using paramiko.SSHClient()
    '''
    conn_session = paramiko.SSHClient()
    conn_session.load_system_host_keys()
    conn_session.connect(ip_addr, port, username, password, look_for_keys = False, allow_agent = False)
    conn = conn_session.invoke_shell()# to keep the session go on

    time.sleep(1)
    conn.send("terminal length 0\n")
    time.sleep(1)

    if conn.recv_ready():
        conn.recv(65535)

    return conn

def send_a_command(conn, command):
    '''
    send a command to an existed conn
    '''
    conn.send(command + "\n")
    time.sleep(1)

    if conn.recv_ready():
        outp = conn.recv(65535)

    return outp

def main():
    '''
    send command "show version" using send_a_command to a connection to router2 created by create_a_conn
    '''

    ip_addr = '184.105.247.71'
    port  = 22
    username = 'pyclass'
    password = '88newclass'
    
    conn1 = create_a_conn(ip_addr, port, username, password)
    print type(conn1)
    outp = send_a_command(conn1, "show version")
    print outp

if __name__ == "__main__":
    main()
