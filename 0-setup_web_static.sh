#!/usr/bin/env bash
# Config it
sudo apt-get update;
if ! [ -e /var/run/nginx.pid ]
then sudo apt-get -y install nginx; fi
if ! [ -e /data/ ];
then sudo mkdir /data/; fi
if ! [ -e /data/web_static/ ];
then sudo mkdir /data/web_static/; fi
if ! [ -e /data/web_static/releases/ ];
then sudo mkdir /data/web_static/releases/; fi
if ! [ -e /data/web_static/shared/ ];
then sudo mkdir /data/web_static/shared/; fi
if ! [ -e /data/web_static/releases/test ];
then sudo mkdir /data/web_static/releases/test; fi

touch /data/web_static/releases/test/index.html;
echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee '/data/web_static/releases/test/index.html';

if ! [ -e /data/web_static/current ];
then sudo ln -s /data/web_static/current /data/web_static/releases/test/;
else
sudo rm /data/web_static/current;
sudo ln -s /data/web_static/current /data/web_static/releases/test/;
fi

sudo chown -R ubuntu:ubuntu /data/;
sudo service nginx restart;
