from datetime import datetime
import datetime
import os
from dotenv import load_dotenv
import webbrowser
import keyboard
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from playsound import playsound
from supabase import create_client, Client
import json
from twilio.rest import Client as Client1
import playsound

load_dotenv()

#Supabase Account URL, Key and calling the Database ID with the supabase Client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_ANON_KEY")
print(url)
print(key)
supabase: Client = create_client(url,key)


#Twilio Account SID, Auth Token and Twilio Phone Number
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('ACCOUNT_AUTH')
twilio_phno = os.environ.get('TWILIO_PHNO')

# Initialize Twilio client
client = Client1(account_sid, auth_token)



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
            query = command.recognize_google(audio,language='en-US') 

            print (f"You Said : {query}")

        except Exception:
            return "lmao"

        return query.lower()
    
    
# Set of all possible if-elif conditions
condition_statements = {
    'hello', 'how are you', 'you need a break', 'youtube search',
    'help', 'google search', 'website', 'launch', 'music', 'wikipedia',
    'whatsapp', 'screenshot', 'open discord', 'open code', 'close discord',
    'close code', 'pause', 'restart', 'mute', 'skip', 'back', 'full screen',
    'film mode', 'youtube tool', 'close this tab', 'open new tab',
    'open new window', 'history', 'download', 'chrome automation',
    'view time table', 'edit time table', 'joke', 'repeat my words',
    'my location', 'hindi', 'alarm'
}

def TaskExe():
    
    global function_history

    def Music():
        Speak("Tell me the Name of the music")
        musicName = takecommand()

        pywhatkit.playonyt(musicName)
            
        Speak("Your song has been started!")
    
                
    def format_phone_number(phone_number):
        # Remove non-digit characters and add country code +91
        cleaned_number = ''.join(filter(str.isdigit, phone_number))
        formatted_number = "+91" + cleaned_number[-10:]  # Keep only the last 10 digits
        return formatted_number
    
                
    def Whatsapp():
        Speak("Whom to send to")
        name=takecommand()
        
        if  'Shobhit' in name:
            Speak("Tell Me the message")
            msg = takecommand()  
            pywhatkit.sendwhatmsg("+917893020941", msg, datetime.datetime.now().hour, datetime.datetime.now().minute+1, 15)  # Sending message
            Speak("Ok sir sending WhatsApp message")

        if 'mummy' in name:
            Speak("Tell Me the message")
            msg = takecommand()
            pywhatkit.sendwhatmsg("+919848245049", msg,datetime.datetime.now().hour, datetime.datetime.now().minute+1, 15)  # Sending message
            Speak("Ok sir sending WhatsApp message")

        else :
            Speak("Tell Me the message")
            msg = takecommand()
            phone = format_phone_number(takecommand())
            pywhatkit.sendwhatmsg(phone, msg, datetime.datetime.now().hour, datetime.datetime.now().minute + 1, 15)  # Sending message
    
    def Emergency():
        
        try:
            # Make a call
            phcall = client.calls.create(
                        twiml='<Response><Say>Hello! This is a call from your child. There is an Emergency!</Say></Response>',
                        to ='+917799902455',
                        from_=twilio_phno
                    )

            print("Call successfully initiated."+phcall.sid)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
        
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
        directory = "C:\\Users\\ACER\\OneDrive\\Pictures\\Screenshots\\"
        if not os.path.exists(directory):
            os.makedirs(directory)  # Create the directory if it doesn't exist
        path1 = os.path.join(directory, path1name)  # Creating the full path
        ss = pyautogui.screenshot()
        ss.save(path1)
        os.startfile(directory)
        Speak("Here is your screenshot")

            
    def ViewTimetable():
        Speak("Which day you want to access")
        query = takecommand()
        query=query.capitalize()
        data = None
        count = None
        if(query=="Monday"): 
            data, count = supabase.table('Timetable').select('*').eq('Day','Monday').execute()
        
        if(query=="Tuesday"):
            data, count = supabase.table('Timetable').select('*').eq('Day','Tuesday').execute()
        if(query=="Wednesday"):
            data, count = supabase.table('Timetable').select('*').eq('Day','Wednesday').execute()
        if(query=="Thursday"):
            data, count = supabase.table('Timetable').select('*').eq('Day','Thursday').execute()
        if(query=="Friday"):
            data, count = supabase.table('Timetable').select('*').eq('Day','Friday').execute()
        if(query=="All"): 
            data, count = supabase.table('Timetable').select('*').execute()
        
        print(data)
        print(count)
        Speak(f"your {query} timetable is {data}")
        
    def EditTimetable():
        Speak("Which day you want to edit")
        query=takecommand()
        query=query.capitalize()
        Speak("Pick a Number to edit the the time slot you want to update")
        # Speak("Pick 1 for 8 am -9am, Pick 2 for 9 am - 10am, Pick 3 for 10 am - 11 am, Pick 4 for 11 am - 12 pm, Pick 5 for 12 pm - 1 pm, Pick 6 for 1 pm - 2 pm, Pick 7 for 2 pm - 3pm, Pick 8 for 3 pm - 4 pm, Pick 9 for 4 pm - 5 pm")
        query_slot=takecommand()
        query_slot=query_slot.replace("number","")
        query_slot=query_slot.replace(" ","")
        query_slot=int(query_slot)
        data = None
        count = None
        Speak("What is the subject you want to keep in the time slot")
        query_sub = takecommand()
        print(query_sub)
        if(query_slot==1):
            data,count=supabase.table('Timetable').update({'8am-9am': query_sub}).eq('Day',query).execute() 
        if(query_slot==2):
            data,count=supabase.table('Timetable').update({'9am-10am': query_sub}).eq('Day',query).execute()
        if(query_slot==3):
            data,count=supabase.table('Timetable').update({'10am-11am': query_sub}).eq('Day',query).execute()
        if(query_slot==4):
            data,count=supabase.table('Timetable').update({'11am-12pm': query_sub}).eq('Day',query).execute()
        if(query_slot==5):
            data,count=supabase.table('Timetable').update({'12pm-1pm': query_sub}).eq('Day',query).execute()
        if(query_slot==6):
            data,count=supabase.table('Timetable').update({'1pm-2pm': query_sub}).eq('Day',query).execute()
        if(query_slot==7):
            data,count=supabase.table('Timetable').update({'2pm-3pm': query_sub}).eq('Day',query).execute()
        if(query_slot==8):
            data,count= supabase.table('Timetable').update({'3pm-4pm': query_sub}).eq('Day',query).execute()
        if(query_slot==9):
            data,count=supabase.table('Timetable').update({'4pm-5pm': query_sub}).eq('Day',query).execute()  
    
        Speak(f"The Timetable has been updated {data}")
        print(count)
        #update checks for column and eq checks for row element in the column day
        
       
    
        
        

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
        query = query.replace("jarvis","")
        
        # Check if the query matches any condition statement
        condition_matched = False
        for condition in condition_statements:
            if query.startswith(condition):
                function_history[condition] = function_history.get(condition, 0) + 1
                condition_matched = True
                break

            # If no condition matched, skip to the next iteration
            if not condition_matched:
                continue
            
        if 'hello' in query :
            Speak ("Hello sir, how may I help you")
            Speak ("I am MARF, your personal AI Assistant")
            # Recommend the three most used functions
            recommended_functions = sorted(function_history, key=function_history.get, reverse=True)[:3]
            Speak("Here are the three most used functions:")
            for func in recommended_functions:
                Speak (func)

        
        elif 'how are you' in query :
            Speak ("I am Fine, what are you doing?")

        elif 'you need a break' in query :
            Speak("Ok sir, please call me anytime you need")
            break

        elif 'youtube search' in query:
            Speak("Ok sir, This is what I have found for your search")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web ='https://www.youtube.com/results?search_query='+query
            webbrowser.open(web)
            Speak("Done Sir")
        
        elif 'help' in query:
            Speak("Contacting the Emergency People")
            Emergency()

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
            query = query.replace("jarvis","")
            query = query.replace("website","")
            
            query = query.replace("open","")
            
            query = query.replace(" ","")
            web = 'https://www.' + query + '.com'
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
        
        elif 'view time table' in query:
            ViewTimetable()
        
        elif 'edit time table' in query:
            EditTimetable()
            
        elif 'joke' in query :
            get = pyjokes.get_joke()
            Speak(get)
        
        elif 'repeat my words' in query:
            Speak("Speak Sir!")
            query = takecommand() 
            Speak (f"You Said : {query}")
        
        elif 'my location' in query:
            Speak ("Ok Sir, Wait A Second")
            webbrowser.open('https://www.google.com/maps/search/my+location/')
            Speak("Done Sir!")
        

        elif 'hindi' in query:
            TakeHindi()
            
        elif 'alarm' in query:
            Speak("Enter the Time")
            time = input("Enter the Time :")

            while True:
                Time_AT = datetime.datetime.now()
                now = Time_AT.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to wake up Gamer")
                    
                    playsound.playsound('E:/MARF_Project/Metal_Pipe.mp3')
                    
                    Speak("Alarm closed ha ha")
                
                elif now > time:
                    break
        
        # Save function history to file before exiting
        with open(function_history_file, "w") as file:
            json.dump(function_history, file)
                
TaskExe()
