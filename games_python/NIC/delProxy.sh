#!/bin/bash
if [[ "$EUID" -ne 0 ]];
then
    echo "Please run as root"
    exit
fi
rm /etc/profile.d/proxy.sh
rm /etc/apt/apt.conf.d/99schneider_proxy
#Most of the time this file ins't added, so this produce an error. This isn't an issue.
rm /etc/systemd/system/docker.service.d/http-proxy.conf
#CHANGE THIS PATH ACCORDING TO YOUR USER, $HOME DON'T WORK BECAUSE OF SUDO
rm /home/user/.docker/config.json
