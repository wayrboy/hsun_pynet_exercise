class telnet_a_conn(object):
    def __init__(self, ip_addr, username, password, port, timeout):
        self.ip_addr = ip_addr
        self.username = username 
        self.password = password
        self.port = port
        self.timeout = timeout


    def create_a_conn(self):
        try:
            self.conn = telnetlib.Telnet(self.ip_addr, self.port, self.timeout)
        except socket.timeout:
            sys.exit("Connection time out")

    def login_a_conn(self):
        output = self.conn.read_until("sername:", self.timeout)
        self.conn.write(self.username + '\n')
        if len(self.password) > 1:
            output += self.conn.read_until("ssword:", self.timeout)
            self.conn.write(self.password + '\n')
            print output
        else:
            print output


            

