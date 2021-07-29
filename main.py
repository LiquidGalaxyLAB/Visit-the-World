#!/usr/bin/python

#Importing libraries####################################################
import os
from geopy.geocoders import Nominatim
from unidecode import unidecode
from time import sleep
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from pynput.keyboard import Key, Controller as KeyboardController

#Definitions###########################################################
geolocator = Nominatim(user_agent="place")
lang = "en"
keyb = KeyboardController()
controller = True
controllerB = True
ModeControl = ""

#Installation Mode Verification########################################
file = open("Visit-the-World/ModeConfig.txt","r")
ModeControl = file.read()
file.close()

if "1" in ModeControl:
   print("Controle 1")
if "2" in ModeControl:
   print("Controle 2")
   exit

#Welcome, first run ##################################################
if controller == True:

    tts = gTTS("Welcome to visit the world!", lang=lang)
    tts.save('Visit-the-World/Sounds/Welcome.mp3')
    playsound('Visit-the-World/Sounds/Welcome.mp3')
    os.remove('Visit-the-World/Sounds/Welcome.mp3')
    sleep(0.2)
    tts2 = gTTS("Enjoy all the functions of this device to discover every corner of the world!", lang=lang)
    tts2.save('Visit-the-World/Sounds/Enjoy.mp3')
    playsound('Visit-the-World/Sounds/Enjoy.mp3')
    os.remove('Visit-the-World/Sounds/Enjoy.mp3')

    controller = False

#Voice recognition function###########################################
def VoiceCommands():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source, duration=1)
        if controllerB == True:
            playsound("Visit-the-World/Sounds/MenuSound.mp3")

        print("Start Speaking!") #apagar
        audio = mic.listen(source)
        print("Working on it") #apagar

    try:
        Command = mic.recognize_google(audio, language=lang)
        UserCommand = unidecode(Command)
        print("You said  {}".format(UserCommand)) #apagar

        p = UserCommand.lower()
        #turn on the green/blue light
        return p

    except sr.UnknownValueError:
        print("I don't understand") #apagar
        # turn on the red light
        return " "

    except sr.RequestError as e:
        print("Impossible to make the call") #apagar
        return " "

#Camera Move Function################################################
def Position_Controller(dataRec):
    controllerB = True
    data = dataRec

    if "zoom out" in data:
        keyb.press(Key.alt)
        keyb.press(Key.page_down)
    elif "zoom in" in data:
        keyb.press(Key.alt)
        keyb.press(Key.page_up)
    elif "move camera right" in data:
        keyb.press(Key.right)  # RIGHT
    elif "move camera left" in data:
        keyb.press(Key.left)  # LEFT
    elif "move camera up" in data:
        keyb.press(Key.up)  # UP
    elif "move camera down" in data:
        keyb.press(Key.down)  # DOWN
    elif "Camera Up" in data:
        keyb.press(Key.ctrl)
        keyb.press(Key.up)
    elif "Camera Down" in data:
        keyb.press(Key.ctrl)
        keyb.press(Key.down)
    elif "Camera Right" in data:
        keyb.press(Key.ctrl)
        keyb.press(Key.right)
    elif "Camera Left" in data:
        keyb.press(Key.ctrl)
        keyb.press(Key.left)
    elif "rollRight" in data:
        keyb.press(Key.shift)
        keyb.press(Key.right)
    elif "rollLeft" in data:
        keyb.press(Key.shift)
        keyb.press(Key.left)
    elif "tilt up" in data:
        keyb.press(Key.shift)
        keyb.press(Key.up)  # UP Tilt
    elif "tilt down" in data:
        keyb.press(Key.shift)
        keyb.press(Key.down)  # DOWN Tilt
    elif "stop" in data:
        keyb.release(Key.alt)
        keyb.release(Key.shift)
        keyb.release(Key.ctrl)
        keyb.release(Key.down)
        keyb.release(Key.right)
        keyb.release(Key.left)
        keyb.release(Key.up)
        keyb.release(Key.page_up)
        keyb.release(Key.page_down)
        print('Stop!')

#Control loop#######################################################
while True:

    p = VoiceCommands()

    if(p == " "):
        controllerB = False
    elif ("hello world" in p) or ("hello words" in p):
        print("Hello welcome!")
        playsound("Visit-the-World/Sounds/HelloWord.mp3")
        controllerB = True
        #turn on the green/blue light

    elif("fly to" in p) or ("flying to" in p) or ("go to" in p) or ("flight to" in p):
        controllerB = True
        print("Ready to fly!")
	#Inserir som de inicio de voo FlyTo

        while p != "stop navigation":
            p = VoiceCommands()

            if p == " ":
                controllerB = False
            elif p == "stop navigation":
                break
            else:
                controllerB = True
                location = geolocator.geocode(p)
                coord = str(location.latitude) + "," + str(location.longitude)
                place = 'search=' + coord
                f = open("/tmp/query.txt", "w")
                f.write(place)
                f.close()

		#Inserir som de voo para flyto
                goingTo = gTTS("going to"+p, lang=lang)
                goingTo.save('Visit-the-World/Sounds/goingTo.mp3')
                playsound('Visit-the-World/Sounds/goingTo.mp3')
                os.remove('Visit-the-World/Sounds/goingTo.mp3')

        controllerB = True

    elif ("change planet" in p) or ("planet change" in p) or ("planets" in p):
        print("Ready to change the planet!")
        playsound("Visit-the-World/Sounds/MenuSound.mp3")

        while p != "return to earth":
            p = VoiceCommands()
            if p == " ":
                controllerB = False
            elif ("return to earth" in p) or ("earth" in p):
                planet = 'planet= earth'
                f = open("/tmp/query.txt", "w")
                f.write(planet)
                f.close()

                changeTo = gTTS("change planet to earth", lang=lang)
                changeTo.save('Visit-the-World/Sounds/changeTo.mp3')
                playsound('Visit-the-World/Sounds/changeTo.mp3')
                os.remove('Visit-the-World/Sounds/changeTo.mp3')

                break
            elif (p == "mars") or (p == "moon"):
                controllerB = True
                planet = 'planet=' + p
                f = open("/tmp/query.txt", "w")
                f.write(planet)
                f.close()

                changeTo = gTTS("change planet to" + p, lang=lang)
                changeTo.save('Visit-the-World/Sounds/changeTo.mp3')
                playsound('Visit-the-World/Sounds/changeTo.mp3')
                os.remove('Visit-the-World/Sounds/changeTo.mp3')

        controllerB = True

    elif ("goodbye" in p) or ("bye-bye" in p) or ("turn of" in p):
        # turn of the sistem
        playsound("Visit-the-World/Sounds/TurnOff.mp3")
        exit()
    else:
        print(p)
        Position_Controller(p)
