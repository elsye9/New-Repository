import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


print('initializing zero')

MASTER = "Elsye"

engine = pyttsx3.init("sapi5")

#kecepatan baca
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) #jenis suara [0] male

#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
        speak("")

#microphone
def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		audio = r.listen(source)
	try:
		text = r.recognize_google(audio)
		print("you said:", text)
		print("Recognizing...")
		query = r.recognize_google(audio, language='id-ID')
		print(f"user said: {query}\n")
	except Exception as e:
		print("say that again please")
		query = None
	return query

#main start here
speak("Hello my name is Zero, i can help you!")
wishMe()
query = takeCommand().lower()

#logic for tasks as per query
if "wikipedia" in query.lower():
	speak("searching wikipedia.....")
	query = query.replace("wikipedia", " ")
	results = wikipedia.summary(query, sentences=1)
	print(results)
	speak(results)
	print("Done!")
	speak("Master, i have done to you.")

elif 'statis' in query.lower():
	speak("searching Statis.....")
	url = "https://saintif.com/rumus-statistika/"
	mozilla_Firefox = "C:/Program Files (x86)/Google/Mozilla Firefox/firefox.exe %s"
	webbrowser.get(mozilla_Firefox).open(url)
	print("done!")
	speak("Master, i have done to you.")

elif "google" in query.lower():
	speak("Searching google")
	url = "google.com"
	mozilla_Firefox = "C:/Program Files (x86)/Google/Mozilla Firefox/firefox.exe %s"
	webbrowser.get(mozilla_Firefox).open(url)
	print("done!")
	speak("Master, i have done to you.")


elif "YouTube" in query.lower():
	speak("Searching Youtube")
	url = "youtube.com"
	mozilla_firefox = "C:/Program Files (x86)/Google/Mozilla Firefox/firefox.exe %s"
	webbrowser.get(mozilla_firefox).open(url)


elif "the time" in query.lower():
	strline = datetime.datetime.now().strftime("%H:%M:%S")
	speak(f"{MASTER} the time is {strline}")
	exit()

#speak bot
elif "Who Handsome" in query.lower():
    speak('you are ver handsome sir ')
elif "who beauty" in query.lower():
    speak('you are beauty but my master very beauty')
elif ""in query.lower():
    speak()
elif "Hi zero! My name is Elsye, and your master. " in query.lower():
	speak(f"Hello{MASTER}, Nice to meet you")
	speak("How are you,Master?")
elif "Fine" in query.lower():
	speak("It's Good to Know that your fine.")
	speak("take care of your health sir")
elif "Who i am" in query.lower():
	speak("If you talk then definitely your human")
elif "Who your master" in query.lower():
	speak("My master is Elsye, she is my creator")
elif "where is" in query:
	query = query.replace("where is", "")
	location = query
	speak("User asked to Locate")
	speak(location)
	webbrowser.open("https://www.google.com / maps / place/" + location + "")
elif "Will you be My friends" in query.lower():
	speak("im not sure about, but I am always with you all the time if you need me")

