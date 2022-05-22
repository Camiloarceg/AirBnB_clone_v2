#!/usr/bin/python3
""" deletes out-of-date archives, using the function do_clean
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
    """ Distributes an archive to your web servers. """
    if not exists(archive_path):
        return False
    path = "/data/web_static/releases/"
    name = archive_path.split('.')[0].split('/')[1]
    dest = path + name
    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dest))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        run('rm -f /tmp/{}.tgz'.format(name))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest))
        return True
    except Exception:
        return False


def deploy():
    """ Creates and distributes an archive to the web servers. """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    """  deletes out-of-date archives """
    if number == 0:
        number = 1
    n_delete = int(
        local("ls -1t versions | wc -l", capture=True)) - int(number)
    files = local("ls -1t versions | tail -{}".format(n_delete), capture=True)
    files_names = files.split("\n")
    for myFile in files_names:
        local('rm versions/{}'.format(myFile))

    n_delete = int(run("ls -1t /data/web_static/releases | wc -l",
                       capture=True)) - int(number)
    files = run("ls -1t /data/web_static/releases | tail -{}".format(
        n_delete), capture=True)
    files_names = files.split("\n")
    for myFile in files_names:
        run('rm /data/web_static/releases/{}'.format(myFile))
