
# NOTE: this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr
import webbrowser
from random import randint

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said '" + text + "'")
    if "when" in text:
        rand_h = str(randint(0, 23)).zfill(2)
        rand_min = str(randint(0, 59)).zfill(2)
        print("I recommend " + rand_h + ":" + rand_min + " o'clock.")
    elif "bill" in text:
        rand_e = str(randint(0, 50))
        print("Your bill is " + rand_e + "€")
    if "demo" in text:
        print("Opening the demo...")
        url = "http://example.com"
        webbrowser.open_new(url)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
