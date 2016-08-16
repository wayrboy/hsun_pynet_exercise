#! /usr/bin/env python

import sys
import socket
import time
import telnetlib

class telnet_a_conn(object):
    '''
    set up a connection and send commands to it and close it
    '''
    def __init__(self, ip_addr, username, password, port, timeout):
        self.ip_addr = ip_addr
        self.username = username 
        self.password = password
        self.port = port
        self.timeout = timeout
        '''
        use Telnet of telnetlib to connect to a device
        '''
        try:
            self.conn = telnetlib.Telnet(self.ip_addr, self.port, self.timeout)
        except socket.timeout:
            sys.exit("Connection time out")

    def login_a_conn(self):
        '''
        login a connection
        '''
        output = self.conn.read_until("sername:", self.timeout)
        self.conn.write(self.username + '\n')
        if len(self.password) > 1:
            output += self.conn.read_until("ssword:", self.timeout)
            self.conn.write(self.password + '\n')
            print output
        else:
            print output

    def send_a_command(self, cmd, sleeptime=1):
        '''
        send a command to this connection
        '''
        cmd = cmd.rstrip()
        self.conn.write(cmd + '\n')
        time.sleep(sleeptime)
        return self.conn.read_very_eager()

    def close_a_conn(self):
        '''
        closet this telnet connection
        '''
        self.conn.close()
            
def main():
    '''
    use the class defined above to set up a connection and play with it
    '''
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'
    port = 23
    timeout = 6

    conn1 = telnet_a_conn(ip_addr, username, password, port, timeout)

    conn1.login_a_conn()
    print  conn1.send_a_command('show ip int br')
    conn1.close_a_conn()

if __name__ == '__main__':
    main()

