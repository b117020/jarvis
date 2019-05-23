import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import wolframalpha
import os

engine = pyttsx3.init()

client = wolframalpha.Client('ETH5J5-7HK4J7HGLH')
def speak(audio):
     engine.say(audio)
     engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening")

    speak("I am Jarvis sir . Please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query} \n")
    except Exception as e:
        #print(e)

        print("Sorry sir, i did'nt get it...please try typing the command...")
        query = str(input('command : '))

    return query

if __name__ == "__main__":
    speak("please enter the password ...")
    password = input('password : ')
    if password == 'devddm' :

        wishMe()

        while True:

            query = takeCommand().lower()


            if 'wikipedia' in query:
                speak("searching wikipedia...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                print(result)
                speak(result)

            elif 'hello' in query:
                speak("hello sir! i hope you are doing fine...")
            elif 'who are you' in query:
                speak("i am Jarvis, your personal assistant, sir...")
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'play music' in query:
                music_dir = 'G:\\songs\\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'stop' in query or 'bye' in query:
                speak("Bye sir, have a good time!!")
                break;


            else:
                query = query
                speak('searching...')
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text
                        print(results)
                        speak('WOLFRAM-ALPHA says :')

                        speak(results)

                    except:
                        results = wikipedia.summary(query, sentences=2)
                        speak('wikipedia says ...')
                        print(results)
                        speak(results)

                except:
                    webbrowser.open('google.com')

    else:
        speak("service denied!! The password you entered was wrong ...")
