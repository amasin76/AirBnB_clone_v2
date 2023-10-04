#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""

    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Create a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(timestamp)

    # Create a tar gzipped archive of the web_static directory
    result = local("tar -cvzf {} web_static".format(filename))

    # Return the name of the archive file on success, otherwise return None
    if result.succeeded:
        return filename
    else:
        return None
