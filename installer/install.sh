#!/bin/bash

echo "Configuring Deploybot"
echo "*********************"

echo "- Checking Root Permissions"
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

echo "- Installing inotify-tools"
apt-get install inotify-tools -y

echo "- Creating Script Directories"
mkdir -p /var/deploybot/watchlist
mkdir -p /opt/deploybot

echo "- Installing Monitor"
cp listener.sh /opt/deploybot/
cp monitor.sh /opt/deploybot/
cp scheduler.sh /opt/deploybot/

cp deploybot-listener.service /etc/systemd/system/deploybot-listener.service
cp deploybot-monitor.service /etc/systemd/system/deploybot-monitor.service
cp deploybot-scheduler.service /etc/systemd/system/deploybot-scheduler.service

echo "- Setting Permissions"
chgrp -R www-data /var/deploybot
chmod -R g+rw /var/deploybot
chmod +x /opt/deploybot/*

echo "- Enabling Monitor"
systemctl enable deploybot-listener.service
systemctl enable deploybot-monitor.service
systemctl enable deploybot-scheduler.service

echo "- Starting Services"
systemctl start deploybot-listener.service
systemctl start deploybot-monitor.service
systemctl start deploybot-scheduler.service
