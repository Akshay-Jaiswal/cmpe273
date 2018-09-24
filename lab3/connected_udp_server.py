from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Server(DatagramProtocol):

    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data.decode(), addr))
        self.upperCase(str(data.decode()))

    def upperCase(self, data):
        data = str(data).upper()
        print("New modified data is : "+str(data))
        host = "127.0.0.1"
        port = 1234
        self.transport.connect(host, port)
        # print(("now we can only send to host %s port %d" % (host, port)))
        self.transport.write(data.encode())  # no need for address


# 0 means any port, we don't care in this case
reactor.listenUDP(1235, Server())
reactor.run()
