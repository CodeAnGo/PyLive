from twisted.internet import reactor
from twisted.application import service
from factories.EchoFactory import EchoServerFactory
from twisted.python import log


class EchoService(service.Service):
    def __init__(self, portNum):
        self.portNum = portNum

    def startService(self):
        log.msg("Started %s on TCP port %d" %(self.__class__.__name__, self.portNum))
        self._port = reactor.listenTCP(self.portNum, EchoServerFactory())

    def stopService(self):
        log.msg("Stopped %s on TCP port %d" %(self.__class__.__name__, self.portNum))
        return self._port.stopListening()
