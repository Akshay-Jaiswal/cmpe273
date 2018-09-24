from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Helloer(DatagramProtocol):
    def startProtocol(self):
        host = "127.0.0.1"
        port = 1235

        self.transport.connect(host, port)
        print(("now we can only send to host %s port %d" % (host, port)))
        self.transport.write("capitalize this".encode())  # no need for address

    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data.decode(), addr))

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")


# 0 means any port, we don't care in this case
reactor.listenUDP(1234, Helloer())
reactor.run()
