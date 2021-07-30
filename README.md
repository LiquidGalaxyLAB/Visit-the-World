# Visit-the-World
 [![github-languages-image](https://img.shields.io/github/languages/top/LiquidGalaxyLAB/Visit-the-World.svg?color=green)]() [![github-language-count-image](https://img.shields.io/github/languages/count/LiquidGalaxyLAB/Visit-the-World.svg)]()  [![github-repo-size-image](https://img.shields.io/github/repo-size/LiquidGalaxyLAB/Visit-the-World.svg?color=yellow)]()
 
 ### __Welcome, know a little more about the project__

Visit the world is a project developed for GSoC 2021. Its main purpose is to help older people who do not have much knowledge of technology to navigate the world through Google Earth using only simple voice commands.

Developed using the LattePanda platform, a small development board with embedded Linux Ubuntu 18.04, a default installation of Google Earth Pro and scripts specially developed for speech detection and recognition and designed to control Google Earth navigation in several different ways.

It can also control a standard Liquid Galaxy installation by simply being connected to the same network as the Liquid Galaxy system.

The project is designed for installation on the LattePanda board, but it can also be installed on conventional computers and also on virtual machines, as long as they have Ubuntu 18.04 as the operating system

 ## __Google Summer Of Code 2021__
 This project was developed within the Google Summer of Code 2021 program. In direct collaboration with the [Liquid Galaxy project](https://www.liquidgalaxy.eu/)

 
 ### Main technologies and languages used
 
* [LattePanda Board](https://www.dfrobot.com/product-1498.html)
* Shell
* Python

## Requirements

- Ubuntu 18.04.5

## How to install and use?

Install git on your computer using:

`sudo apt install git`

Clone the project repository using:

`git clone https://github.com/LiquidGalaxyLAB/Visit-the-World.git`

Enter the repository directory using:

`cd Visit-the-World`

Run the install script using the commands:

`chmod +x install.sh`

`./install.sh`

Accept all requests with `y` + `Enter`

- After finishing all installation, press `Enter` to process.
  Google Earth will open and then your computer will restart.

- After the computer restarts log out and log in again using I3 WM as screen manager

- On the first screen that appears, just press `Enter` twice.
- Press `Wind + Enter` key to open a terminal.
- Enter the directory folder `cd Visit-the-World` e execute o comando:
- `./i3Config`

The computer will restart once again opening Google Earth in Fullscreen mode and already with the voice commands enabled so you can navigate the world!

## Main available voice commands

- Zoom More
- Zoom out
- Move camera right
- Move camera left
- Look up
- Look down
- Rotate camera right
- Rotate camera left
- Orbit
- Stop or Break (To stop camera movements)

- Hello world (To start voice commands)
- Fly to or Go to (To start navigation) After entering the menu, just say the name of the city or tourist place you want to fly to.
- Stop navigation (To exit flight mode)
- Change planet (To change the planet) Whenever you want to change the planet, just call this command and then say which planet you want to go to Earth, Mars or Moon.
- Return to earth - You need to access the Change Planet menu to be able to return to Earth with this command.
- Goodbye or Turn of - This command will close the application and shut down the computer.
- Liquid Galaxy - This command just closes the application and waits for the command to start browsing a Liquid Galaxy installation (The user will need to enter the necessary information from the master PC)

## Complete documentation
...


Copyright 2020 [Otávio Jeus França Oliveira](https://www.linkedin.com/in/otaviojfoliveira/)
