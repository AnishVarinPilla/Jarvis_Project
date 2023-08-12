import webbrowser

import pyttsx3
import pywhatkit
import speech_recognition as sr

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
            query = query.replace("%20","")
            query = query.replace("open","")
            web2 = "https://www." + query + ".com"
            webbrowser.open(web2)
            Speak("Launched")

        elif 'launch' in query:
            Speak("Tell me The name of the website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir")


TaskExe()