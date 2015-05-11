import gevent
from gevent.queue import Queue


class RemoteService(object):

    def __init__(self):
        super(RemoteService, self).__init__()
        self.command_queue = Queue()

    def _push_command(self, command):
        self.command_queue.put(command)

    def _run(self):
        while True:
            command = self.command_queue.get()
            self.handle(command)

    def serve(self):
        gevent.spawn(self._run)
