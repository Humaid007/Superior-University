import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import openai
from gtts import gTTS
import pygame
import os
from threading import Thread
import musiclibrary  

newsapi = os.getenv("NEWSAPI_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove(filename)

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    Thread(target=play_audio, args=('temp.mp3',)).start()

def aiProcess(command):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses, please."},
            {"role": "user", "content": command},
        ]
    )
    return response.choices[0].message["content"]

def processCommand(c):
    c_lower = c.lower()
    if "open google" in c_lower:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open facebook" in c_lower:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook.")
    elif "open youtube" in c_lower:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "play" in c_lower:
        song = c_lower.replace("play", "").strip()
        if song in musiclibrary.music:  
            webbrowser.open(musiclibrary.music[song])
            speak(f"Playing {song}.")
        else:
            speak("I could not find that song in the library.")
    elif "news" in c_lower:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                for article in articles[:5]:  # Limit to 5 headlines
                    speak(article['title'])
            else:
                speak("I couldn't fetch the news right now.")
        except Exception as e:
            speak("There was an error fetching the news.")
    elif "exit" in c_lower:
        speak("Goodbye!")
        exit()
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise once
        while True:
            try:
                print("Listening for 'Jarvis'...")

                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Yes?")
                    print("Jarvis active, listening for a command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print(f"Command received: {command}")
                    processCommand(command)
            except sr.UnknownValueError:
                print("Sorry, I did not catch that.")
                speak("Sorry, I did not catch that.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                speak("There was an issue with the speech recognition service.")
            except Exception as e:
                print(f"An error occurred: {e}")
                speak("An unexpected error occurred.")
