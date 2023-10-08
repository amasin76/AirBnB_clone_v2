#!/usr/bin/python3
# Deletes out-of-date archives

from fabric.api import *

env.hosts = ['52.87.232.85', '52.91.148.64']
env.user = "ubuntu"


def clean_local_archives(number):
    """
    Deletes out-of-date local archives.
    """
    local("cd versions/ && ls -t | tail -n +{} | sudo xargs rm -rf"
          .format(number))


def clean_remote_releases(number):
    """
    Deletes out-of-date remote releases.
    """
    path = "/data/web_static/releases"
    run("cd {} && ls -t | tail -n +{} | sudo xargs rm -rf"
        .format(path, number))


@task
def do_clean(number=0):
    """
    deletes out-of-date archives
    """
    num = int(number)
    if num < 1:
        num = 2
    else:
        num += 1
    clean_local_archives(num)
    clean_remote_releases(num)
