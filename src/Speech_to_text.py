#TODO: Get this script to work
import speech_recognition as sr
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Buddy: listening....")
        audio = r.listen(source)
        try:
            query = r.recognize_googel(audio)
            print(f"master:{query}")
            return query
        except:
            print("Try again")
print(command())

