import datetime
import os
import webbrowser
import keyboard
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from playsound import playsound
from pydictionary import Dictionary
from supabase import create_client, Client
import json

url: str = os.environ.get("https://bpvqpkigcjnqplpbdisx.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJwdnFwa2lnY2pucXBscGJkaXN4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyOTU2MzEsImV4cCI6MjAyMjg3MTYzMX0.MKlMzhFGw4Bo6_eiAkgnIXMxrV0Zt8fkoIr6Cc8Sxfo")
supabase: Client = create_client(url,key)

# Define a global variable to store the file path
function_history_file = "function_history.json"

# Load function history from file if available
try:
    with open(function_history_file, "r") as file:
        function_history = json.load(file)
except FileNotFoundError:
    
    function_history = {}
    
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

        except Exception:
            return "None"

        
        return query.lower()
    
    


def TaskExe():
    
    global function_history

    def Music():
        Speak("Tell me the Name of the music")
        musicName = takecommand()

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
            Diction=Dictionary(prob,3)
            result = Diction.meanings()
            Speak(f"The meaning for {prob} is {result}")

        elif 'synonym' in prob:
            prob = prob.replace('what is the synonym of ', '')
            prob = prob.replace('jarvis', '')
            Diction=Dictionary(prob,3)
            result = Diction.synonyms(prob)
            Speak(f"The meaning for {prob} is {result}")
        
        elif 'antonym' in prob:
            prob = prob.replace('what is the antonym of ', '')
            prob = prob.replace('jarvis', '')
            Diction=Dictionary(prob,3)
            result = Diction.antonyms(prob)
            Speak(f"The meaning for {prob} is {result}")
            
    def ViewTimetable():
        Speak("Which day you want to access")
        query = takecommand()
        
        if(query=="Monday"): response = supabase.table('Timetable').select("Mon").execute() 
        if(query=="Tuesday"):response = supabase.table('Timetable').select("Tues").execute()
        if(query=="Wednesday"):response = supabase.table('Timetable').select("Wed").execute()
        if(query=="Thursday"):response = supabase.table('Timetable').select("Thur").execute()
        if(query=="Friday"):response = supabase.table('Timetable').select("Fri").execute()
        if(query=="All"): response = supabase.table('Timetable').select("*").execute()
        
        print(response)
        Speak(f"your {query} timetable is {response}")
        
    def EditTimetable():
        Speak("Which day you want to edit")
        query=takecommand()
        Speak("Pick a Number to edit the the time slot you want to update")
        Speak("Pick 1 for 8 am -9am, Pick 2 for 9 am - 10am, Pick 3 for 10 am - 11 am, Pick 4 for 11 am - 12 pm, Pick 5 for 12 pm - 1 pm, Pick 6 for 1 pm - 2 pm, Pick 7 for 2 pm - 3pm, Pick 8 for 3 pm - 4 pm, Pick 9 for 4 pm - 5 pm")
        query_slot= int(takecommand())
        Speak("What is the subject you want to keep in the time slot")
        query_sub = takecommand()
        if(query_slot==1):
            supabase.table('Timetable').update({'8am-9am': query_sub}).eq('Day',query).execute()
        if(query_slot==2):
            supabase.table('Timetable').update({'9am-10am': query_sub}).eq('Day',query).execute()
        if(query_slot==3):
            supabase.table('Timetable').update({'10am-11am': query_sub}).eq('Day',query).execute()
        if(query_slot==4):
            supabase.table('Timetable').update({'8am-9am': query_sub}).eq('Day',query).execute()
        if(query_slot==5):
            supabase.table('Timetable').update({'8am-9am': query_sub}).eq('Day',query).execute()
        if(query_slot==6):
            supabase.table('Timetable').update({'8am-9am': query_sub}).eq('Day',query).execute()
        if(query_slot==7):
            supabase.table('Timetable').update({'8am-9am': query_sub}).eq('Day',query).execute()  
    
        Speak("The Timetable has been updated")
        
    
        
        

    def TakeHindi():
        command = sr.Recognizer()           #taking in the voice input and recognizing what we are saying
        with sr.Microphone() as source :    #assiging Mircrophone as the source of Voice Input

            print ('Listening........')
            command.pause_threshold =1
            audio = command.listen(source)

            try :
                print ("Recognizing.......")

                #processes the input you have given and decrypts it using google recognized language
                query = command.recognize_google(audio,language='hi') 

                print (f"You Said : {query}")

            except Exception:
                return "None"


        
        return query.lower()

    
        
    while True:

        query = takecommand()
        if 'hello' in query :
            Speak ("Hello sir, how may I help you")
            Speak ("I am JARVIS, your personal AI Assistant")
            # Recommend the three most used functions
            recommended_functions = sorted(function_history, key=function_history.get, reverse=True)[:3]
            Speak("Here are the three most used functions:")
            for func in recommended_functions:
                Speak (func)

        
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
            Speak (f"According to wikipedia : {wiki}")

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
        
        elif 'view timetable' in query:
            ViewTimetable()
        
        elif 'edit timetable' in query:
            EditTimetable()
            
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

        elif 'hindi' in query:
            TakeHindi()
            
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
                
                elif now > time:
                    break
        
        if query in function_history:
            function_history[query] += 1
        else:
            function_history[query] = 1
        
        # Save function history to file before exiting
        with open(function_history_file, "w") as file:
            json.dump(function_history, file)
                
                    


TaskExe()
