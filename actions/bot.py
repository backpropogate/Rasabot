import speech_recognition as sr
import sys
from gtts import gTTS
import subprocess
import playsound
import requests

chat_bot_message = ""
message = ""

while chat_bot_message != "Bye" or chat_bot_message != "thanks":
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        print("How can I help you Creator? ")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio)
            print("did you say :{}".format(message))
        except:
            print("Sorry could not hear you")
    if len(message) == 0:
        continue
    print("Just a sec..")
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})
    print("Here is your answer:", end='  ')
    for i in r.json():
        chat_bot_message = i['text']
        print(f"{chat_bot_message}")
    obj = gTTS(text=chat_bot_message)
    obj.save("greeting.mp3")
    print('saved')

    playsound.playsound("greeting.mp3")

    # rasa endpoints
    # rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
