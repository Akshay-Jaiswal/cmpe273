from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastPingPong(DatagramProtocol):

    def startProtocol(self):
        """
        Called after protocol has started listening.
        """
        # Set the TTL>1 so multicast will cross router hops:
        self.transport.setTTL(5)
        # Join a specific multicast group:
        self.transport.joinGroup("228.0.0.4")

    def datagramReceived(self, datagram, address):
        print("Datagram %s received from %s" % (datagram.decode(), repr(address)))
        if datagram.decode() == "Client Ping" or datagram.decode() == "Client: Ping":
            # Rather than replying to the group multicast address, we send the
            # reply directly (unicast) to the originating port:
            self.transport.write("Server: Pong".encode(), address)


# We use listenMultiple=True so that we can run multicast_udp_server.py and
# multicast_udp_client.py on same machine:
reactor.listenMulticast(9999, MulticastPingPong(), listenMultiple=True)
reactor.run()
