from flask import Flask, request
from flask_sockets import Sockets

import gevent

from .osc import OSCService, OSCServer
from .routing import MessageRouter

app = Flask(__name__)
sockets = Sockets(app)

router = MessageRouter()
osc_service = OSCService(router.broadcast)
osc_service.serve()

osc_server = OSCServer(':9000')
osc_server.set_handler(osc_service.handle)
osc_server.serve()

@sockets.route('/events')
def outbox(ws):
    router.register(ws)
    while not ws.closed:
        gevent.sleep()
