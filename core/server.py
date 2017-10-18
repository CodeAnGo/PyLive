from twisted.internet import reactor
from twisted.python import log
from services.EchoService import EchoService
from datetime import datetime
import sys

# log.startLogging(open("logs/" + datetime.now().strftime('network_framework_%H_%M_%d_%m_%Y.log'), "w"))
log.startLogging(sys.stdout)

EchoService = EchoService(1234)
EchoService.startService()

reactor.run()
