import datetime
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voice',voices[0].id)

#print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


    pass
def wishMe():
    hour =int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning!")
       
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")

            else
            speak("Good evening")
        



def takeCommand

    
if __name__=="__main__":
    # speak("hello")
    wishMe()








