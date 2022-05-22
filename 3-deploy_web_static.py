#!/usr/bin/python3
""" Fabric script based on the file 2-do_deploy_web_static.py that creates and
    distributes an archive to the web servers
"""
from fabric.api import run, put, env, local
from datetime import datetime
from os.path import exists, isdir

env.hosts = ["54.91.227.223", "107.22.140.255"]


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


def deploy():
    """ Creates and distributes an archive to the web servers. """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
