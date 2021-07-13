#!/bin/bash

echo "Installing Dependencies..."
sudo apt net-tools
sudo apt install portaudio19-dev python-all-dev
sudo apt install python-pip
sudo apt install gdebi

echo "Installing Libraries"
pip install gTTS
pip install SpeechRecognition
pip install playsound
pip install pynput
pip install PyAudio
pip install unidecode
pip install geopy


echo "Installing Google Earth..."
sudo gdebi google-earth-pro-stable_current_amd64.deb


echo "Editing Drivers.Ini"

sudo rm -f /opt/google/earth/pro/drivers.ini
sudo mv drivers.ini /opt/google/earth/pro
sudo rm -f google-earth-pro-stable_current_amd64.deb


