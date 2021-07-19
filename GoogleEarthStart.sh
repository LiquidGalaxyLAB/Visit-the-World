#!/bin/bash

sudo rm -f ~/.config/Google/GoogleEarthPro.conf
sudo cp ~/Visit-the-World/GoogleEarthPro.conf ~/.config/Google

google-earth-pro &

python ~/Visit-the-World/main.py 

