import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def taking_command():
    with sr.Microphone() as source:
        print("Listening..")
        audio=recognizer.listen(source)


    try :
        print("Recognizing...")
        command=recognizer  .recognize_google(audio)   
        print(f"You said:{command}")
        return command.lower()
    except sr.UnknownValueError :
        print( "Speak Loud I couldn't hear You !")
        return ""
    except sr.RequestError as e:
        print( "Error while Speaking". format(e))

if __name__=="__main__":
    speak("Say 'Jarvis' to activate me. ")

    while True:
        trigger=taking_command()    

        if "jarvis" in trigger:
            speak("how can I help you sir")
            command=taking_command()

            if "time" in command:
                current_time = datetime.now().strftime("%I:%M %p")
                speak(f"The current time is {current_time}")
            
            elif "youtube" in command:
                webbrowser.open("https://youtube.com")
                speak("opening Youtube.")
                break
            else:   
                speak("Speak Loud I couldn't hear you.")