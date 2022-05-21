#!/usr/bin/env bash
# Sets web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<!DOCTYPE html>
<head>
</head>
<body>
    Holberton School
</body>
<html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
f_config="/etc/nginx/sites-available/default"
sed -i "/listen 80 default_server;/a location /hbnb_static/ {alias /data/web_static/current/;}" $f_config
sudo service nginx restart
