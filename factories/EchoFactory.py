from twisted.internet.protocol import Factory
from protocols.Echo import EchoServer, EchoClient


class EchoServerFactory(Factory):
    def buildProtocol(self, addr):
        return EchoServer()


class EchoClientFactory(Factory):
    def startedConnecting(self, connector):
        print 'Started to connect.'

    def buildProtocol(self, addr):
        print 'Connected.'
        return EchoClient()

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection.  Reason:', reason

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed. Reason:', reason
