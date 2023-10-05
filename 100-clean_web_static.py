#!/usr/bin/python3
# Deletes out-of-date archives

from fabric.api import local, run, env
import os

env.hosts = ['52.87.232.85', '52.91.148.64']


def do_clean(number=0):
    """
    Delete out-of-date archives.

    Parameters:
    number (int): The number of archives to keep.
    """

    number = int(number)
    if number < 2:
        number = 2

    local("ls -t versions | tail -n +{} | xargs rm -f --".format(number))
    run("ls -t /data/web_static/releases | tail -n +{} | xargs rm -rf --"
        .format(number))
