from twisted.internet.protocol import Protocol
from twisted.python import log

class EchoServer(Protocol):
    def dataReceived(self, data):
        log.msg("Received %d Bytes of Data" %(len(data)))
        self.sendData(data)

    def sendData(self, data):
        self.transport.write(data)
        log.msg("Sent %d Bytes of Data" %(len(data)))

class EchoClient(Protocol):
    def connectionMade(self):
        log.msg("Connected to server!")
        self.sendData("Hello World!")

    def dataReceived(self, data):
        log.msg("Received %d Bytes of Data" %(len(data)))
        self.sendData(data)

    def sendData(self, data):
        self.transport.write(data)

