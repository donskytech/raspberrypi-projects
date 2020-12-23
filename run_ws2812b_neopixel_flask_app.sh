#!/bin/bash

export PYTHONPATH="$PWD:"

mkdir -p /var/log/gunicorn/

chmod  777 /var/log/gunicorn/

echo "Starting WS2812B Neopixel Flask Application..."

gunicorn -w 1 -b 0.0.0.0:5000 ws2812b_neopixel_flask_final.app:app --error-logfile /var/log/gunicorn/error.log --access-logfile /var/log/gunicorn/access.log --capture-output --log-level debug
