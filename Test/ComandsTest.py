import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

import keyboard
from pynput.keyboard import Key, Controller as KeyboardController

keyb = KeyboardController()

count = 1  # parametro para frase inicial
mic = sr.Recognizer()  # seta microfone para reconhecer


def Position_Controller(dataRec):
    data = dataRec

    if "zoom out" in data:
        keyb.press(Key.page_down)
    elif "zoom in" in data:
        keyb.press(Key.page_up)
    elif "right" in data:
        keyb.press(Key.right)  # RIGHT
    elif "left" in data:
        keyb.press(Key.left)  # LEFT
    elif "up" in data:
        keyb.press(Key.up)  # UP
    elif "down" in data:
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
        keyb.release(Key.shift)
        keyb.release(Key.ctrl)
        keyb.release(Key.down)
        keyb.release(Key.right)
        keyb.release(Key.left)
        keyb.release(Key.up)
        keyb.release(Key.page_up)
        keyb.release(Key.page_down)
        print('parou')


if count == 1:

    tts = gTTS("To start say a command", lang='en')
    tts.save('start.mp3')
    playsound('start.mp3')

    count = 0

with sr.Microphone() as source:
    mic.adjust_for_ambient_noise(source)  # ajuste para ruido

    while True:
        try:
            playsound('notificaion.mp3')
            audio = mic.listen(source)
            command = mic.recognize_google(audio, language='en')
            print("You say the command: " + command)

            Position_Controller(command)

            tts = gTTS(command, lang='en')
            tts.save('audios/start.mp3')
            playsound('audios/start.mp3')
            os.remove('audios/start.mp3')


        except:
            print("I did not understand")
