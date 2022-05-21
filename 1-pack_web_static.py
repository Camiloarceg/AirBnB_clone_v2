#!/usr/bin/python3
"""
Script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo.
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """Packs a local web_static folder to .tgz format for deploy """

    local("mkdir -p versions")
    t = datetime.now()
    tgz = "versions/web_static_"
    tgz += "{}{}{}{}{}{}.tgz".format(t.year, t.month, t.day,
                                     t.hour, t.minute, t.second)
    tgz_file = "tar -cvzf {} web_static".format(tgz)
    if local(tgz_file).failed:
        return None
    return tgz
