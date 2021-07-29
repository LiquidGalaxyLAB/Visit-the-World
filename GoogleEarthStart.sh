#!/bin/bash

sudo rm -f ~/.config/Google/GoogleEarthPro.conf
sudo cp ~/Visit-the-World/ConfigFiles/GoogleEarthPro.conf ~/.config/Google

amixer -D pulse sset Master on   #Output Sound Turn on  
amixer -D pulse sset Master 95%  #Output Sound level 
amixer set Capture cap		 #Set Microphone capture On
amixer set Capture 90%           #Microphone level 

killall googleearth-bin 

google-earth-pro &

python ~/Visit-the-World/main.py 

