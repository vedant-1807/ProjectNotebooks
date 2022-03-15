import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good morning!')
    elif 12 <= hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak("I am Jarvis sir! Please tell me how can I help you?")


def takeCommand():
    """It takes microphone input form the user and returns the string output"""
    r = sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source, phrase_time_limit=0)

    try:
        print("Recognizing...")
        queries = r.recognize_google(audio, language='en-in').lower()
        print(f"User said: {queries} \n")

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned

    return queries


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 586)
    server.ehlo()
    server.starttls()
    server.login('bheniavedant@gmail.com', 'Bheniavedant18')
    server.sendmail('bheniavedant@gmail.com', to, content)
    server.close()


if __name__ == "__main__":

    wishMe()
    print("initialising...")
    while True:
        query = takeCommand().lower()  # Converting user query into lower case
        # logics for executing tasks based on query

        if 'wikipedia' in query.lower():  # if wikipedia found in the query then this block will be executed
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'search' in query:
            speak('what do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search   # this triggers the search command in google search.
            webbrowser.get().open(url)

        elif 'find location' in query:
            speak('what place do you want to search for?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location  # this triggers the search command in the google maps.
            webbrowser.get().open(url)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            googlePath = ("C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe")
            os.startfile(googlePath)

        elif 'play music' in query:
            music_dir = "C:\\Users\\Vedant Bhenia\\Music\\favourites"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif ' the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'email to vedant' in query:
            try:
                speak('what should I say?')
                content = takeCommand()
                to = "bheniavedant@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully")

            except Exception as e:
                print(e)
                speak("Sorry Email cannot be sent!")

        elif "remind" in query:
            speak("what should i remind you")
            messageT = takeCommand()
            speak("ok, so when should i remind you.")
            timeOfReminder = takeCommand()
            while True:
                current_time = time.strftime("%H:%M:%S")
                if current_time == timeOfReminder:
                    print(current_time)
                    break

            toaster = ToastNotifier()
            toaster.show_toast(messageT, duration=10)


        elif 'how are you' in query:
            speak("I am fine, Thank you!")
            speak("How are you?, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "notepad" in query:
            os.system("notepad.exe")

        elif 'camera' in query:
            os.system('start microsoft.windows.camera:')
        elif 'prompt' in query:
            os.system('cmd.exe')

        elif 'play' in query:
            pywhatkit.playonyt(query)
        elif 'who is' in query:
            pywhatkit.search(query)
        elif 'tell me about' in query:
            pywhatkit.search(query)
        elif 'open browser and type' in query:
            pywhatkit.search(query)

