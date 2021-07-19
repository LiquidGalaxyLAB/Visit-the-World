#!/bin/bash

cat << "EOM"
 _   _  _       _  _     _____  _              _    _               _      _ 
| | | |(_)     (_)| |   |_   _|| |            | |  | |             | |    | |
| | | | _  ___  _ | |_    | |  | |__    ___   | |  | |  ___   _ __ | |  __| |
| | | || |/ __|| || __|   | |  | '_ \  / _ \  | |/\| | / _ \ | '__|| | / _` |
\ \_/ /| |\__ \| || |_    | |  | | | ||  __/  \  /\  /| (_) || |   | || (_| |
 \___/ |_||___/|_| \__|   \_/  |_| |_| \___|   \/  \/  \___/ |_|   |_| \__,_|
 
https://github.com/LiquidGalaxyLAB/Visit-the-World
-------------------------------------------------------------
EOM

echo "Installing Dependencies..."
sudo apt net-tools
sudo apt install portaudio19-dev python-all-dev
sudo apt install python-pip
sudo apt install gdebi
sudo apt install i3 i3blocks

echo "Installing Libraries"
pip install gTTS
pip install SpeechRecognition
pip install playsound
pip install pynput
pip install PyAudio
pip install unidecode
pip install geopy

echo "Screen Dimming Setting"
gsettings set org.gnome.desktop.session idle-delay 0

echo "Installing Google Earth..."
sudo gdebi google-earth-pro-stable_current_amd64.deb


echo "Editing Drivers.Ini..."
sudo rm -f /opt/google/earth/pro/drivers.ini
sudo mv drivers.ini /opt/google/earth/pro
sudo rm -f google-earth-pro-stable_current_amd64.deb

echo "Editing I3 Config..."
sudo rm -f /home/panda/.config/i3/config
sudo mv config /home/panda/.config/i3/config

chmod 755 GoogleEarthStart.sh

echo "Visit the World installation completed! :-)"
echo "Press ENTER key to reboot now"
read
reboot

exit 0

