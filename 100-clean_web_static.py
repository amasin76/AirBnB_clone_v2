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

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions && ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} && ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
