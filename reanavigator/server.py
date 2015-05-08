from flask import Flask, request
from flask_sockets import Sockets

import gevent

from .player import PlayerService
from .routing import MessageRouter

app = Flask(__name__)
sockets = Sockets(app)

router = MessageRouter()
player_service = PlayerService(router.broadcast)
player_service.serve()


@app.route('/play')
def play():
    song = request.args.get('song')
    player_service.play(song)
    return ''


@sockets.route('/notes')
def outbox(ws):
    router.register(ws)
    while not ws.closed:
        gevent.sleep()
