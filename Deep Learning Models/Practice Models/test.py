# Example: Using Google STT in Python
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source)
    text = r.recognize_google(audio, language="en-US")  # Hindi
    print("You said:", text)
