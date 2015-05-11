import gevent


class MessageRouter(object):

    def __init__(self):
        self.clients = []

    def register(self, ws):
        self.clients.append(ws)

    def broadcast(self, message):
        for client in self.clients:
            gevent.spawn(client.send, message)
