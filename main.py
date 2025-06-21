import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        speak("Opening facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open github" in c.lower():
        speak("Opening github")
        webbrowser.open("https://www.github.com")
    elif "open instagram" in c.lower():
        speak("Opening instagram")
        webbrowser.open("https://www.instagram.com/t4run_11")
        #Love from Tarun
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLib.music[song]
        webbrowser.open(link)
     
    else: 
        #let AI handle the request
        pass


if __name__ == "__main__":
    speak("Welcome to Suar......")
    
    while True:

        # recognize speech using Google
        try:
            # obtain audio from the microphone
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            print("You said : " + r.recognize_google(audio))
            word = r.recognize_google(audio)

            if "suar" in word.lower():
                speak("Yes Sir, how can I help you?")
                #listen for the command
                with sr.Microphone() as source:
                    print("Suar Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
