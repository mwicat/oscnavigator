#!/bin/bash

gunicorn --reload -k flask_sockets.worker reanavigator.server:app
