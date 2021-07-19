#!/bin/bash


echo "Editing I3 Config..."
sudo rm -f ~/.config/i3/config
sudo mv config ~/.config/i3/config

reboot
