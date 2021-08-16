import os
from tkinter import *

file = open("Visit-the-World/ConfigFiles/LGConfig.txt","r")
LG_File = file.read()
LG_IP = LG_File.split('\n',1)[0]
LG_PASSWORD = LG_File.split('\n',1)[1]
file.close()

def changeParameters(ip,password):
    lg_ip = ip
    lg_password = password
    f = open("Visit-the-World/ConfigFiles/LGConfig.txt", "w")
    f.write(lg_ip + '\n')
    f.write(lg_password)
    f.close()

    file = open("Visit-the-World/ConfigFiles/LGConfig.txt","r")
    LG_File = file.read()
    LG_IP = LG_File.split('\n',1)[0]
    LG_PASSWORD = LG_File.split('\n',1)[1]
    file.close()


class Application:
    def __init__(self, master=None):
        self.standardFont = ("Arial", "10")

        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 20
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 100
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer["padx"] = 20
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer["pady"] = 30
        self.fourthContainer.pack()

        self.fifthContainer = Frame(master)
        self.fifthContainer["pady"] = 5
        self.fifthContainer.pack()

        self.sixthContainer = Frame(master)
        self.sixthContainer["padx"] = 20
        self.sixthContainer.pack()

        self.seventhContainer = Frame(master)
        self.seventhContainer["padx"] = 20
        self.seventhContainer.pack()

        self.eighthContainer = Frame(master)
        self.eighthContainer["padx"] = 20
        self.eighthContainer.pack()
        #################################################################################################
        self.title = Label(self.firstContainer, text="LIQUID GALAXY CONNECTION")
        self.title["font"] = ("Arial", "20", "bold")
        self.title.pack()

        self.lgLabel = Label(self.secondContainer, text="          Master IP: ", font=self.standardFont)
        self.lgLabel.pack(side=LEFT)
        self.ip = Entry(self.secondContainer)
        self.ip["width"] = 20
        self.ip["font"] = self.standardFont
        self.ip.pack(side=LEFT)

        self.passwordLabel = Label(self.thirdContainer, text="Master Password:", font=self.standardFont)
        self.passwordLabel.pack(side=LEFT)
        self.password = Entry(self.thirdContainer)
        self.password["width"] = 20
        self.password["font"] = self.standardFont
        self.password["show"] = "*"
        self.password.pack(side=LEFT)

        self.pushButton1 = Button(self.fourthContainer, text="Enter Data", font=("Calibri", "12"))
        self.pushButton1["command"] = self.button1Press
        self.pushButton1["width"] = 20
        self.pushButton1.pack()

        self.pushButton = Button(self.fifthContainer, text="Connect With Liquid Galaxy", font=("Calibri", "12"))
        self.pushButton["command"] = self.buttonPress
        self.pushButton["width"] =30
        self.pushButton.pack()

        self.message = Label(self.fifthContainer, text="", font=self.standardFont)
        self.message.pack()

        self.masterIpLabel = Label(self.sixthContainer, text="Master IP: ", font=self.standardFont)
        self.masterIpLabel.pack(side=LEFT)
        self.iplabel = Label(self.sixthContainer, text=LG_IP, font=self.standardFont)
        self.iplabel.pack(side=LEFT)

        self.masterPasswordLabel = Label(self.seventhContainer, text="Master Password: ", font=self.standardFont)
        self.masterPasswordLabel.pack(side=LEFT)
        self.Passwordlabel = Label(self.seventhContainer, text= '*' * len(LG_PASSWORD), font=self.standardFont)
        self.Passwordlabel.pack(side=LEFT)

        self.AlertLabel = Label(self.eighthContainer, text="ALERT ! ", font=("Arial", "12", "bold"),fg="red")
        self.AlertLabel.pack(side=LEFT)
        self.AlertMsg = Label(self.eighthContainer,
                              text="If the IP and password data fields are invalid or empty it will not be possible to connect with Liquid Galaxy",
                              font=self.standardFont,
                              bg="yellow")
        self.AlertMsg.pack(side=LEFT)
    #######################################################################################################
    #Método verificar senha
    def buttonPress(self):
        file = open("Visit-the-World/ConfigFiles/LGConfig.txt", "r")
        LG_File = file.read()
        LG_IP = LG_File.split('\n', 1)[0]
        LG_PASSWORD = LG_File.split('\n', 1)[1]
        file.close()
        if LG_IP != "invalid ip" and LG_PASSWORD != "invalid passwrod":
            self.message["text"] = "connecting"
            os.system("python ~/Visit-the-World/lg-voice.py")
        else:
            self.message["text"] = "Enter data before connecting"

    def button1Press(self):
        ip = self.ip.get()
        password = self.password.get()
        if(ip == "")or(password==""):
            changeParameters("invalid ip", "invalid passwrod")
            self.iplabel["text"] = "invalid ip"
            self.Passwordlabel["text"] = "invalid passwrod"
        else:
            changeParameters(ip, password)
            file = open("Visit-the-World/ConfigFiles/LGConfig.txt", "r")
            LG_File = file.read()
            LG_IP = LG_File.split('\n', 1)[0]
            LG_PASSWORD = LG_File.split('\n', 1)[1]
            file.close()
            self.iplabel["text"] = LG_IP
            self.Passwordlabel["text"] = '*' * len(LG_PASSWORD)

root = Tk()
root.wm_title("Liquid Galaxy")
root.geometry("800x500")
Application(root)
root.mainloop()