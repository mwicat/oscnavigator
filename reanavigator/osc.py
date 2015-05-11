import gevent
from gevent.server import DatagramServer

import calendar
import time

from pythonosc import osc_packet, dispatcher

from .services import RemoteService


class OSCServer(DatagramServer):

    def __init__(self, *args, **kw):
        super(OSCServer, self).__init__(*args, **kw)
        self.dispatcher = dispatcher.Dispatcher()

    def set_handler(self, handler):
        self.dispatcher.set_default_handler(handler)

    def handle(self, data, address):
        # Get OSC messages from all bundles or standalone message.
        try:
            packet = osc_packet.OscPacket(data)
            for timed_msg in packet.messages:
                now = calendar.timegm(time.gmtime())
                handlers = self.dispatcher.handlers_for_address(
                    timed_msg.message.address)
                if not handlers:
                    continue
                # If the message is to be handled later, then so be it.
                if timed_msg.time > now:
                    time.sleep(timed_msg.time - now)
                for handler in handlers:
                    if handler.args:
                        handler.callback(
                            timed_msg.message.address, handler.args, *timed_msg.message)
                    else:
                        handler.callback(timed_msg.message.address, *timed_msg.message)
        except osc_packet.ParseError:
            pass

    def serve(self):
        gevent.spawn(self.serve_forever)


class OSCService(RemoteService):

    def __init__(self, cb):
        super(OSCService, self).__init__()
        self.cb = cb

    def handle(self, command, *args):
        print 'got command', command, args
