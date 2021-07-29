#!/bin/bash

cat << "EOM"
 _   _  _       _  _     _____  _              _    _               _      _ 
| | | |(_)     (_)| |   |_   _|| |            | |  | |             | |    | |
| | | | _  ___  _ | |_    | |  | |__    ___   | |  | |  ___   _ __ | |  __| |
| | | || |/ __|| || __|   | |  | '_ \  / _ \  | |/\| | / _ \ | '__|| | / _` |
\ \_/ /| |\__ \| || |_    | |  | | | ||  __/  \  /\  /| (_) || |   | || (_| |
 \___/ |_||___/|_| \__|   |_|  |_| |_| \___|   \/  \/  \___/ |_|   |_| \__,_|
 
https://github.com/LiquidGalaxyLAB/Visit-the-World
-------------------------------------------------------------


EOM

#Sudo Access Start
sudo -v

echo ""

# Parameters
INSTALLATION_MODE="2"

read -p "Installation Mode (1 == LattePanda) (2 == regular PC): " INSTALLATION_MODE


if [ $INSTALLATION_MODE == "1" ]; then
    echo -e " \nYOU CHOSE OPTION $INSTALLATION_MODE, INSTALL ON LATTEPANDA BOARD \n"
    read -p "Press any key to continue or Ctrl+C to stop"
    echo "1" >ModeConfig.txt

elif [ $INSTALLATION_MODE == "2" ]; then
    echo -e " \nYOU CHOSE OPTION $INSTALLATION_MODE, INSTALL ON A REGULAR PC \n"
    echo "2" >ModeConfig.txt
    read -p "Press any key to continue or Ctrl+C to stop"
fi


echo -e "\nAudio settings..."

amixer -D pulse sset Master on   #Output Sound Turn on  
amixer -D pulse sset Master 95%  #Output Sound level 
amixer set Capture cap		 #Set Microphone capture On
amixer set Capture 90%           #Microphone level 

echo -e "\nChecking for system updates...\n"
sudo apt update
echo -e "\nChecking for system upgrades...\n"
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
gsettings set org.gnome.desktop.session idle-delay 0 #Set not to turn off screen 

echo "Installing Google Earth..."
sudo gdebi google-earth-pro-stable_current_amd64.deb


echo "Editing Drivers.Ini..."
sudo rm -f /opt/google/earth/pro/drivers.ini
sudo cp ConfigFiles/drivers.ini /opt/google/earth/pro
sudo rm -f google-earth-pro-stable_current_amd64.deb #Removing google-earth.deb


sudo chmod 755 GoogleEarthStart.sh
sudo chmod 755 i3config.sh

# Only for installations on the LattePanda board
#Enable the Serial communication 
if [ $INSTALLATION_MODE == "1" ]; then
    sudo chmod o+rw /dev/ttyACM0 
fi


echo -e "\nVisit the World installation completed! :-) \n"
echo "Press ENTER key to reboot now"
read
google-earth-pro &
sleep 15

killall googleearth-bin 
reboot

exit 0

#gnome-session-quit --force

