import os
import webbrowser
import time

import keyboard
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from PyDictionary import PyDictionary as Diction
import datetime
from playsound import playsound

Assistant = pyttsx3.init('sapi5') #creating a variable to take in the Microsoft Voice Lib assigned with the id = sapi5

voices = Assistant.getProperty('voices') #taking the voices which are available into a array in voices variable

print (voices) #printing the voices to find out which voices are available

Assistant.setProperty('voices',voices[0].id) #taking in the default voice by using the setProperty syntax
Assistant.setProperty('rate',170) #setting the rate at which the VA will speak

def Speak(audio):  #Defined a Method for the Code to Speak

    print("   ")
    Assistant.say(audio)
    print(f":{audio}")
    print("   ")
    Assistant.runAndWait()

def takecommand(): #Defined a Method for the Code to take in Voice Input (possible with the PyAudio Package for the code to access the Microphone)

    command = sr.Recognizer()           #taking in the voice input and recognizing what we are saying
    with sr.Microphone() as source :    #assiging Mircrophone as the source of Voice Input

        print ('Listening........')
        command.pause_threshold =1
        audio = command.listen(source)

        try :
            print ("Recognizing.......")

            #processes the input you have given and decrypts it using google recognized language
            query = command.recognize_google(audio,language='en-in') 

            print (f"You Said : {query}")

        except Exception as Error:
            return "None"

        
        return query.lower()


def TaskExe():

    def Music():
        Speak("Tell me the Name of the music")
        musicName = takecommand()

        if 'loca' in musicName :

            os.startfile('E:\Songs\loca.mp3')

        elif 'red dead' in musicName :

            os.startfile('E:\Songs\ red dead.mp3')

        else:
            pywhatkit.playonyt(musicName)
            
        Speak("Your song has been started!")

    
    def Whatsapp():
        Speak("Tell me the name of the person ")
        name = takecommand()

        if 'Shobit' or 'Shobhit' in name:
            Speak("Tell Me the message")
            msg = takecommand()
            Speak("Tell me the Hour")
            hour = int(takecommand())
            Speak("Tell me the minute")
            min = int(takecommand())
            
            pywhatkit.sendwhatmsg("+917893020941",msg,hour,min,10)
            Speak("Ok sir sending WhatsApp message")

        elif 'mummy' in name:
            Speak("Tell Me the message")
            msg = takecommand()
            Speak("Tell me the Hour")
            hour = int(takecommand())
            Speak("Tell me the minute")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919848245049",msg,hour,min,10)
            Speak("Ok sir sending WhatsApp message")

        else :
            Speak("Tell me the phone number")
            phone = takecommand()
            ph = '+91' + phone
            ph = ph.replace(" ","")
            Speak("Tell Me the message")
            msg = takecommand()
            Speak("Tell me the Hour")
            hour = int(takecommand())
            Speak("Tell me the minute")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,10)
            Speak("Ok sir sending WhatsApp message")
    
    def OpenApps():

        Speak("Ok Sir, Wait a Second")
        
        if 'code' in query:
            os.system("E:\\Microsoft VS Code\\Code.exe")

        elif 'discord' in query:
            os.system("C:\\Users\\ACER\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")

        Speak("Your Command has been executed")

    def CloseApps():
        Speak("Ok sir, wait a second")

        if 'code' in query :
            os.system("TASKKILL / F/ im Code.exe")
        if 'discord' in query :
            os.system ("TASKKIL/ F/ im Update.exe --processStart Discord.exe")
        
        Speak("Your Command has been executed")

    def YoutubeAutomation():

        Speak("What's your command ?")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')
        
        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')
        
        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')
        
        Speak ("Done Sir")

    def ChromeAutomation():
        Speak("Chrome Automate Mode On")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release ('ctrl + w')

        elif 'open new tab' in command :
            keyboard.press_and_release ('ctrl + t')

        elif 'open new window' in command :
            keyboard.press_and_release ('ctrl + n')
        
        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')
        
        elif 'download' in command :
            keyboard.press_and_release('ctrl + j')

    def screenshot():
        Speak("What should I name it.")
        path = takecommand()
        path1name = path + ".png"
        path1 = "C:\\Users\\ACER\\OneDrive\\Pictures\\Screenshots\\" +path1name #creating a path link to save the screenshot
        ss = pyautogui.screenshot()
        ss.save(path1)
        os.startfile("C:\\Users\\ACER\\OneDrive\\Pictures\\Screenshots")
        Speak("Here is your screenshot")

    def Dict():
        Speak("Tell me the word that you want me to define")
        prob = takecommand()

        if 'meaning' in prob:
            prob = prob.replace('what is the meaning of ', '')
            prob = prob.replace('jarvis', '')

            result = Diction.meaning(prob)
            Speak(f"The meaning for {prob} is {result}")

        elif 'synonym' in prob:
            prob = prob.replace('what is the synonym of ', '')
            prob = prob.replace('jarvis', '')

            result = Diction.synonym(prob)
            Speak(f"The meaning for {prob} is {result}")
        
        elif 'antonym' in prob:
            prob = prob.replace('what is the antonym of ', '')
            prob = prob.replace('jarvis', '')

            result = Diction.antonym(prob)
            Speak(f"The meaning for {prob} is {result}")

    while True:

        query = takecommand()
        if 'hello' in query :
            Speak ("Hello sir, how may I help you")
            Speak ("I am JARVIS, your personal AI Assistant")
        
        elif 'how are you' in query :
            Speak ("I am Fine, what are you doing?")

        elif 'you need a break jarvis' in query :
            Speak("Ok sir, please call me anytime you need")
            break

        elif 'youtube search' in query:
            Speak("Ok sir, This is what I have found for your search")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web ='https://www.youtube.com/results?search_query='+query
            webbrowser.open(web)
            Speak("Done Sir")

        elif 'google search' in query:
            Speak ("This is what I Found for your search")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done Sir!")

        elif 'website' in query:
            Speak("Ok sir Launching...")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            
            query = query.replace("open","")
            
            query = query.replace(" ","")
            web2 = "https://www."+query+".com"
            webbrowser.open(web2)
            Speak("Launched")

        elif 'launch' in query:
            Speak("Tell me The name of the website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir")

        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia......")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak ("According to wikipedia : {wiki}")

        elif 'whatsapp' in query:
            Whatsapp()
            
        elif 'screenshot' in query:
            screenshot()

        elif 'open discord' in query:
            query = query.replace("open ","")
            OpenApps()

        elif 'open code' in query:
            query = query.replace("open ","")
            OpenApps()

        elif 'close discord' in query:
            query = query.replace("close ","")
            CloseApps()

        elif 'close code' in query:
            query = query.replace("close ","")
            CloseApps()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')
        
        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')
        
        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAutomation()

        elif 'close this tab' in query:
            keyboard.press_and_release ('ctrl + w')

        elif 'open new tab' in query :
            keyboard.press_and_release ('ctrl + t')

        elif 'open new window' in query :
            keyboard.press_and_release ('ctrl + n')
        
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
        
        elif 'download' in query :
            keyboard.press_and_release('ctrl + j')

        elif 'chrome automation' in query:
            ChromeAutomation()
        
        elif 'joke' in query :
            get = pyjokes.get_joke()
            Speak(get)
        
        elif 'repeat my words' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak (f"You Said : {jj}")
        
        elif 'my location' in query:
            Speak ("Ok Sir, Wait A Second")
            webbrowser.open('https://www.google.com/maps/@17.7324576,83.3041052,15z?entry=ttu')
            Speak("Done Sir!")
        
        elif 'dictionary' in query:
            Dict()

        elif 'alarm' in query:
            Speak("Enter the Time")
            time = input(": Enter the Time :")

            while True:
                Time_AT = datetime.datetime.now()
                now = Time_AT.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to wake up Gamer")
                    for i in range(6):
                        playsound('Metal_Pipe.mp3')
                        time.sleep(1)
                    
                    Speak("Alarm closed ha ha")
                    


TaskExe()