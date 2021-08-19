#!/usr/bin/python

#Importing libraries####################################################
import os
from geopy.geocoders import Nominatim
from unidecode import unidecode
from time import sleep
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from paramiko import SSHClient
import paramiko

#Definitions###########################################################
geolocator = Nominatim(user_agent="place")
lang = "en"
controller = True
controllerB = True
ModeControl = ""
sound = "Visit-the-World/Sounds/TurnOff.mp3"

##SSH CONNECTION#######################################################
file = open("Visit-the-World/ConfigFiles/LGConfig.txt","r")
LG_File = file.read()
LG_IP = LG_File.split('\n',1)[0]
LG_PASSWORD = LG_File.split('\n',1)[1]
file.close()

class SSH:
    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname = LG_IP, username='lg',password = LG_PASSWORD)

    def exec_cmd(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print (stderr.read())
        else:
            print (stdout.read())

#Welcome, first run ##################################################
if controller == True:

    playsound(sound)
    sound = "Visit-the-World/Sounds/HelloWord.mp3"

    tts = gTTS("Welcome to visit the world!", lang=lang)
    tts.save('Visit-the-World/Sounds/Welcome.mp3')
    playsound('Visit-the-World/Sounds/Welcome.mp3')
    os.remove('Visit-the-World/Sounds/Welcome.mp3')
    sleep(0.2)
    tts2 = gTTS("Start controlling Liquid Galaxy using just your voice", lang=lang)
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
    ssh = SSH()
    controllerB = True
    sound = "Visit-the-World/Sounds/MoveCamera.mp3"
    data = dataRec

    if ("zoom out" in data) or ("remove zoom" in data) or ("back off" in data) : #Zoom -
        playsound(sound)
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keydown Alt+Page_Down")
    elif ("zoom in" in data) or ("zoom more" in data) or ("zoom open" in data) : #Zoom +
        playsound(sound)
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keydown Alt+Page_Up")
    elif ("move camera right" in data) or ("move right" in data) or ("camera right" in data):# RIGHT
        playsound(sound)
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keydown Alt+Right")
    elif ("move camera left" in data) or ("move left" in data) or ("camera left" in data): # LEFT
        playsound(sound)
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keydown Alt+Left")
    elif ("move camera up" in data) or ("look up" in data) or ("looking up" in data) or ("go up" in data) or ("up" in data): # UP
        playsound(sound)
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keydown Alt+Up")
    elif ("move camera down" in data) or ("look down" in data) or ("looking down" in data) or ("go down" in data) or ("down" in data): # DOWN
        playsound(sound)
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keydown Alt+Down")
    elif ("rotate right" in data) or ("rotate camera right" in data) or ("rotate to right" in data) :# Look RIGHT
        playsound(sound)
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keydown Ctrl+Right")
    elif ("rotate left" in data) or ("rotate camera left" in data) or ("rotate to left" in data) : # Look LEFT
        playsound(sound)
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keydown Ctrl+Left")
    elif ("below" in data) or ("drop" in data): # Tilt Down
        playsound(sound)
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keydown Shift+Alt+Down")
    elif ("above" in data) : # Tilt Up
        playsound(sound)
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keydown Shift+Alt+Up")
    elif ("orbit" in data) or ("look around" in data) or ("looking around" in data) or ("make an orbit" in data) or ("make circle" in data):	# Orbit
        playsound(sound)
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keydown Shift+Alt+Right")
    elif ("stop" in data) or ("break" in data) or ("stop movement" in data):
        playsound(sound)
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keyup Alt+Up")
        #Para baixo
        ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keyup Alt+Down")
        #para direita
    	ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keyup Alt+Right")
        #para esquerda
    	ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keyup Alt+Left")
        #Zoom in
    	ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keyup Alt+Page_Down")
        #Zoom out
    	ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keyup Alt+Page_Up")
        #Girar no eixo da camera
    	ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keyup Ctrl+Right")
        #Girar no eixo da camera
    	ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keyup Ctrl+Left")
        #Orbit
    	ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keyup Shift+Alt+Right")
        #Tilt Up
    	ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keyup Shift+Alt+Up")
        #Tilt Down
    	ssh.exec_cmd("export DISPLAY=:0.0 &&xdotool keyup Shift+Alt+Down")


#Control loop#######################################################
while True:
    #ssh = SSH()
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

                    send = 'echo ' + "'" + place +"'" + '>/tmp/query.txt'

                    ssh = SSH()
                    ssh.exec_cmd(send)
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
        playsound(sound)

        while p != "return to earth":
            p = VoiceCommands()
            if p == " ":
                controllerB = False
            elif ("return to earth" in p) or ("earth" in p):
                planet = 'planet= earth'

                sendPlanet = 'echo ' + "'" + planet +"'" + '>/tmp/query.txt'

                ssh = SSH()
                ssh.exec_cmd(sendPlanet)

                playsound(sound)
                changeTo = gTTS("change planet to earth", lang=lang)
                changeTo.save('Visit-the-World/Sounds/changeTo.mp3')
                playsound('Visit-the-World/Sounds/changeTo.mp3')
                os.remove('Visit-the-World/Sounds/changeTo.mp3')
                break
            elif (p == "mars") or (p == "moon"):
                controllerB = True
                planet = 'planet=' + p

                sendPlanet = 'echo ' + "'" + planet +"'" + '>/tmp/query.txt'

                ssh = SSH()
                ssh.exec_cmd(sendPlanet)

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
    elif(p == "liquid galaxy turn off") or (p == "galaxy off") or (p == "galaxy exit"):
        sound = "Visit-the-World/Sounds/TurnOff.mp3"
        playsound(sound)
        exit()
    else:
        print(p)
        Position_Controller(p)
