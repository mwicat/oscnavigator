import logging
logging.basicConfig()
logger = logging.getLogger('oscnavcli')

import argh
from argh import arg

from pythonosc import osc_message_builder
from pythonosc import udp_client


class ClientProxy(object):

    def __init__(self, client):
        self.client = client

    def __getattr__(self, attr):
        if attr == 'client':
            return self.__dict__['client']
        else:
            return lambda *args: send(self.client, '/' + attr, *args)


def send(client, addr, *args):
    msg = osc_message_builder.OscMessageBuilder(address=addr)
    for arg in args:
        msg.add_arg(arg)
    msg = msg.build()
    client.send(msg)


@arg('-h', '--host')
@arg('-p', '--port')
def shell(host='127.0.0.1', port=9000):
    client = udp_client.UDPClient(host, port)
    c = ClientProxy(client)
    from IPython import embed
    embed()


def main():
    parser = argh.ArghParser()
    parser.add_commands([shell])
    parser.dispatch()


if __name__ == '__main__':
    main()
