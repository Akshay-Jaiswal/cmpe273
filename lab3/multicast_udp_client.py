from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastPingClient(DatagramProtocol):

    def startProtocol(self):
        # Join the multicast address, so we can receive replies:
        self.transport.joinGroup("228.0.0.4")
        # Send to 228.0.0.4:9999 - all listeners on the multicast address
        # (including us) will receive this message.
        self.transport.write("Hello World".encode(), ("228.0.0.4", 9999))

    def datagramReceived(self, datagram, address):
        print("Datagram %s received from %s" % (datagram.decode(), repr(address)))


reactor.listenMulticast(9999, MulticastPingClient(), listenMultiple=True)
reactor.run()
