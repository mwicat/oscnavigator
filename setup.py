#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='reanavigator',
      version='0.7.1',
      description='Web application for learning the musical scales',
      author='mwicat',
      author_email='mwicat@gmail.com',
      include_package_data=True,
      zip_safe=False,
      packages=find_packages(),
      install_requires=['argh',
                        'Flask',
                        'flask-Cache',
                        'Flask-RESTful',
                        'Flask-Sockets',
                        'gunicorn',
                        'gevent',
                        'gevent-websocket',
                        'music21',
                        'progressbar2',
                        'redis',
                        'sqlalchemy'],
      entry_points={'console_scripts':
                    ['reanavigatord = reanavigator.scripts.reanavigatord:main']
                    }
)
