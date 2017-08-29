import pyttsx3

text=input("enter text to speak")
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()