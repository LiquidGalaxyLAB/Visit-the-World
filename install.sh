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

# Parameters
INSTALLATION_MODE="1"

read -p "Installation Mode (1 == LattePanda) (2 == regular PC): " INSTALLATION_MODE


if [ $INSTALLATION_MODE == "1" ]; then
    echo ""
    echo "YOU CHOSE OPTION $INSTALLATION_MODE, INSTALL ON LATTEPANDA BOARD"
    echo ""
    read -p "Press any key to continue or Ctrl+C to stop"
    echo "1" >ModeConfig.txt

elif [ $INSTALLATION_MODE == "2" ]; then
    echo ""
    echo "YOU CHOSE OPTION $INSTALLATION_MODE, INSTALL ON A REGULAR PC"
    echo ""
    echo "2" >ModeConfig.txt
    read -p "n Press any key to continue or Ctrl+C to stop"
fi

read -p "Parar teste" #apagar

echo "Checking for system updates..."
sudo apt update
echo "Checking for system upgrades..."
sudo apt upgrade -f

echo "Installing Dependencies..."
sudo apt install net-tools
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
pip install paramiko

echo "Screen Dimming Setting"
gsettings set org.gnome.desktop.session idle-delay 0

echo "Installing Google Earth..."
sudo gdebi google-earth-pro-stable_current_amd64.deb


echo "Editing Drivers.Ini..."
sudo rm -f /opt/google/earth/pro/drivers.ini
sudo cp ConfigFiles/drivers.ini /opt/google/earth/pro
sudo rm -f google-earth-pro-stable_current_amd64.deb #Removing google-earth.deb


chmod 755 GoogleEarthStart.sh
chmod 755 i3config.sh

# Only for installations on the LattePanda board
if [ $INSTALLATION_MODE == "1" ]; then
    chmod o+rw /dev/ttyACM0 
fi


echo "Visit the World installation completed! :-)"
echo "Press ENTER key to reboot now"
read
google-earth-pro &
sleep 10

reboot

exit 0

#gnome-session-quit --force

