#!/bin/bash

gunicorn --reload -k flask_sockets.worker oscnavigator.server:app
