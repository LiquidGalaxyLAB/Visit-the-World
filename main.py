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
sound = "Visit-the-World/Sounds/TurnOff.mp3"

#Installation Mode Verification########################################
#file = open("Visit-the-World/ModeConfig.txt","r")
#ModeControl = file.read()
#file.close()

#if "1" in ModeControl:
#  print("Controll 1")

#Welcome, first run ##################################################
if controller == True:

    playsound(sound)
    sound = "Visit-the-World/Sounds/HelloWord.mp3"

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
            playsound(sound)

        print("Start Speaking!") #delete
        audio = mic.listen(source)
        print("Working on it") #delete

    try:
        Command = mic.recognize_google(audio, language=lang)
        UserCommand = unidecode(Command)
        print("You said  {}".format(UserCommand)) #delete

        p = UserCommand.lower()
        #turn on the green/blue light
        return p

    except sr.UnknownValueError:
        print("I don't understand") #delete
        # turn on the red light
        return " "

    except sr.RequestError as e:
        print("Impossible to make the call") #delete
        return " "

#Camera Move Function################################################
def Position_Controller(dataRec):
    controllerB = True
    sound = "Visit-the-World/Sounds/MoveCamera.mp3"
    data = dataRec

    if ("zoom out" in data) or ("remove zoom" in data) or ("close zoom" in data) or ("back off" in data) : #Zoom -
        playsound(sound)
	keyb.press(Key.alt)
        keyb.press(Key.page_down)
    elif ("zoom in" in data) or ("zoom more" in data) or ("open zoom" in data) or ("zoom open" in data) or ("closer" in data) or ("advance" in data): #Zoom +
	playsound(sound)        
	keyb.press(Key.alt)
        keyb.press(Key.page_up)
    elif ("move camera right" in data) or ("right" in data) or ("move right" in data) or ("look to the right" in data) or ("look to right" in data) or ("looking to right" in data) or ("rotate right" in data) or ("go right" in data): # RIGHT
	playsound(sound)	
	keyb.press(Key.alt)
        keyb.press(Key.right)  
    elif ("move camera left" in data) or ("left" in data) or ("move left" in data) or ("look to the left" in data) or ("look to left" in data) or ("looking to left" in data) or ("rotate left" in data) or ("go left" in data): # LEFT
	playsound(sound)	
	keyb.press(Key.alt)
        keyb.press(Key.left)  
    elif ("move camera up" in data) or ("look up" in data) or ("looking up" in data) or ("walk up" in data) or ("go up" in data) or ("spin up" in data) or ("up" in data): # UP
	playsound(sound)	
	keyb.press(Key.alt)
        keyb.press(Key.up)  
    elif ("move camera down" in data) or ("look down" in data) or ("looking down" in data) or ("walk down" in data) or ("go down" in data) or ("spin down" in data) or ("down" in data): # DOWN
	playsound(sound)	
	keyb.press(Key.alt)
        keyb.press(Key.down)  
    elif ("camera right" in data) or ("rotate camera right" in data):# Look RIGHT
	playsound(sound)        
	keyb.press(Key.ctrl)
        keyb.press(Key.right)
    elif ("camera left" in data) or ("rotate camera left" in data): # Look LEFT
	playsound(sound)        
	keyb.press(Key.ctrl)
        keyb.press(Key.left)
    elif ("orbit" in data) or ("look around" in data) or ("looking around" in data) or ("make an orbit" in data) or ("make circle" in data):	# Orbit
	playsound(sound)        
	keyb.press(Key.shift)
	keyb.press(Key.alt)
        keyb.press(Key.right)
    elif ("stop" in data) or ("break" in data) or ("stop movement" in data):
	playsound(sound)        
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
	sound = "Visit-the-World/Sounds/HelloWord.mp3"
        #turn on the green/blue light

    elif("fly to" in p) or ("flying to" in p) or ("go to" in p) or ("flight to" in p):
        controllerB = True
        print("Ready to fly!")#delete
	#FlyTo sound
	sound = "Visit-the-World/Sounds/FlyTo.mp3"
	playsound(sound)

        while p != "stop navigation":
            p = VoiceCommands()

            if p == " ":
                controllerB = False
            elif ("stop navigation" in p) or ("hello world" in p) or ("hello words" in p):
		sound = "Visit-the-World/Sounds/HelloWord.mp3"
		playsound(sound)
                break
            else:
                controllerB = True
		try:
                    location = geolocator.geocode(p)
                    coord = str(location.latitude) + "," + str(location.longitude)
                    place = 'search=' + coord
                    f = open("/tmp/query.txt", "w")
                    f.write(place)
                    f.close()
		
		    playsound(sound)
                    goingTo = gTTS("going to"+p, lang=lang)
                    goingTo.save('Visit-the-World/Sounds/goingTo.mp3')
                    playsound('Visit-the-World/Sounds/goingTo.mp3')
                    os.remove('Visit-the-World/Sounds/goingTo.mp3')
		except:
		
		    notFound = gTTS("Location not found, try another place")
                    notFound.save('Visit-the-World/Sounds/notFound.mp3')
                    playsound('Visit-the-World/Sounds/notFound.mp3')
                    os.remove('Visit-the-World/Sounds/notFound.mp3')

        controllerB = True

    elif ("change planet" in p) or ("planet change" in p) or ("planets" in p):
        print("Ready to change the planet!")
	sound = "Visit-the-World/Sounds/MenuSound.mp3"

        while p != "return to earth":
            p = VoiceCommands()
            if p == " ":
                controllerB = False
            elif ("return to earth" in p) or ("earth" in p):
                planet = 'planet= earth'
                f = open("/tmp/query.txt", "w")
                f.write(planet)
                f.close()
 
		playsound(sound)
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

		playsound(sound)
                changeTo = gTTS("change planet to" + p, lang=lang)
                changeTo.save('Visit-the-World/Sounds/changeTo.mp3')
                playsound('Visit-the-World/Sounds/changeTo.mp3')
                os.remove('Visit-the-World/Sounds/changeTo.mp3')

		sound = "Visit-the-World/Sounds/HelloWord.mp3"
 		break

        controllerB = True

    elif (p == "goodbye") or (p == "bye-bye") or (p == "turn of"):
        # turn of the sistem
        playsound("Visit-the-World/Sounds/TurnOff.mp3")
	playsound(sound)
        os.system("shutdown -h now")
    elif(p == "liquid galaxy") or (p == "galaxy"):
 	sound = "Visit-the-World/Sounds/TurnOff.mp3"
	playsound(sound)
	os.system("killall googleearth-bin")
	exit()
    else:
        print(p)
        Position_Controller(p)
