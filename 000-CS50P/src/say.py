import pyttsx3

engine = pyttsx3.init()
this = input("what is this?")
engine.say(this)
engine.runAndWait()

