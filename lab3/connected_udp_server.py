from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Server(DatagramProtocol):

    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data.decode(), addr))


# 0 means any port, we don't care in this case
reactor.listenUDP(1235, Server())
reactor.run()
