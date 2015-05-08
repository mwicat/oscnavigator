from gevent import sleep

from .services import RemoteService


class PlayerService(RemoteService):

    def __init__(self, cb):
        super(PlayerService, self).__init__()
        self.cb = cb

    def play(self, song):
        self._push_command(song)

    def handle(self, song):
        for i in range(10):
            note = '%s' % i
            self.cb(note)
            sleep(1)
