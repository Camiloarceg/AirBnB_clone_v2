#!/usr/bin/python3
""" do_pack function """

from fabric.api import run, put, env
from datetime import datetime
from os.path import exists

env.hosts = ["54.91.227.223", "107.22.140.255"]


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        file_not_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run("mkdir -p {}{}".format(path, file_not_ext))
        run("tar xzf /tmp/{} -C {}{}/".format(file_name, path, file_not_ext))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_not_ext))
        run("rm /tmp/{}".format(file_name))
        run("rm /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, file_not_ext))
        return True
    except Exception:
        return False
