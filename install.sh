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

amixer -D pulse sset Master on >/dev/null 2>&1  #Output Sound Turn on  
amixer -D pulse sset Master 95% >/dev/null 2>&1 #Output Sound level 
amixer -D pulse sset Capture cap >/dev/null 2>&1  	#Set Microp hone capture On
amixer -D pulse sset Capture 85% >/dev/null 2>&1          #Microphone level 

echo -e "\nChecking for system updates...\n"
sudo apt -y update
echo -e "\nChecking for system upgrades...\n"
sudo apt -y upgrade -f

echo "Installing Dependencies..."
sudo apt install -y python3-tk lsb lsb-core net-tools portaudio19-dev python-all-dev python-pip gdebi i3 i3blocks

echo "Installing Libraries"
pip install gTTS SpeechRecognition playsound pynput PyAudio unidecode geopy paramiko

echo "Screen Dimming Setting"
gsettings set org.gnome.desktop.session idle-delay 0 #Set not to turn off screen 

echo "Installing Google Earth..."
sudo gdebi google-earth-pro-stable_current_amd64.deb

echo "Google earth file removed"
sudo rm -f google-earth-pro-stable_current_amd64.deb #Removing google-earth.deb

echo "Changing path of temporary files"
cache="CachePath=/home/$USER/.googleearth/Cache"
kmlpath="KMLPath=/home/$USER/.googleearth"

sed -i "s|CachePath=|$cache|" /ConfigFiles/GoogleEarthPro.conf
sed -i "s|KMLPath=|$kmlpath|" /ConfigFiles/GoogleEarthPro.conf

echo "Editing config files..."
#Drivers.ini Changes
sudo rm -f /opt/google/earth/pro/drivers.ini
sudo cp ConfigFiles/drivers.ini /opt/google/earth/pro
#Google Earth config change
sudo rm -f ~/.config/Google/GoogleEarthPro.conf
sudo rmdir ~/.config/Google >/dev/null 2>&1
sudo mkdir ~/.config/Google
sudo cp ~/Visit-the-World/ConfigFiles/GoogleEarthPro.conf ~/.config/Google
#I3 Window manager config file
sudo mkdir ~/.config/i3
sudo cp ~/Visit-the-World/ConfigFiles/config ~/.config/i3

sudo chmod 755 GoogleEarthStart.sh

# Only for installations on the LattePanda board
#Enable the Serial communication 
if [ $INSTALLATION_MODE == "1" ]; then
    sudo chmod o+rw /dev/ttyACM0 
fi


echo -e "\nVisit the World installation completed! :-) \n"
echo "Press ENTER key to make logout now"
read

#logout
sudo pkill -9 -u $USER

exit 0

