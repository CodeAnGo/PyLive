from twisted.internet import reactor
from factories.EchoFactory import EchoClientFactory
from twisted.python import log
from datetime import datetime
import sys

# log.startLogging(open("logs/" + datetime.now().strftime('client_%H_%M_%d_%m_%Y.log'), "w"))
log.startLogging(sys.stdout)
reactor.connectTCP("127.0.0.1", 1234, EchoClientFactory())
reactor.run()
