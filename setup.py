#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='oscnavigator',
      version='0.0.1',
      description='Web application to help navigate tracks in mixer',
      author='mwicat',
      author_email='mwicat@gmail.com',
      include_package_data=True,
      zip_safe=False,
      packages=find_packages(),
      dependency_links=['http://github.com/mwicat/python2-osc/tarball/python2#egg=python2-osc'],
      install_requires=['argh',
                        'Flask',
                        'flask-Cache',
                        'Flask-RESTful',
                        'Flask-Sockets',
                        'gunicorn',
                        'gevent',
                        'gevent-websocket',
                        'python2-osc'],
      entry_points={'console_scripts':
                    ['oscnavcli = oscnavigator.scripts.oscnavcli:main']
                    }
)
