import logging
logging.basicConfig()
logger = logging.getLogger('scaletrainerd')

import argh
from argh import arg


def track():
    print 'track'


def main():
    parser = argh.ArghParser()
    parser.add_commands([syncdb, filldb, validate, shell])
    parser.dispatch()


if __name__ == '__main__':
    main()
