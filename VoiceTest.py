import speech_recognition as sr
import pyttsx3
import time
import datetime

# Initialize Speaking Engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)    # speaking speed
engine.setProperty('volume', 0.9)

def speak(audio):
    print("Speaking:", audio)
    engine.say(audio)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening... (Bolo ab)")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=6, phrase_time_limit=6)
    
    try:
        query = r.recognize_google(audio, language='en-in')
        print("You said:", query)
        return query.lower()
    except:
        # print("Sorry, samajh nahi aya")
        return None

# Greeting
speak("Hello Junaid, main aapka voice assistant hoon")
speak("Ab bolo, kya chahiye?")

# Main Loop
while True:
    query = listen()
    
    if query is None:
        continue

    # Commands
    if "hello" in query or "hi" in query:
        speak("Hello! Kaise ho aap?")

    elif "name" in query:
        speak("Mera naam Grok hai")

    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Abhi time hai {current_time}")

    elif "date" in query:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Aaj ki date hai {today}")

    elif "how are you" in query:
        speak("Main theek hoon, aap kaise ho?")

    elif "stop" in query or "exit" in query or "band kar" in query or "bye" in query:
        speak("Okay, Goodbye! Take care")
        break

    else:
        speak("Sorry, abhi yeh command samajh nahi aya. Kuch aur try karo")