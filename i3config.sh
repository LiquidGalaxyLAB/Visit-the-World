#!/bin/bash


echo "Editing I3 Config..."
sudo rm -f ~/.config/i3/config
sudo cp config ~/.config/i3/config

reboot
