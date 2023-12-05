import random
from speech_recognition import Recognizer, Microphone
from datetime import datetime
import requests
from playsound import playsound
import os

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/cpN9L5YLPgARXYoBnTLE"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "aed1d1b745dda092b7257c694d3ec143"
  }


def Speech(text):
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.7,
        "style": 0
        }
    }
    response = requests.post(url, json=data, headers=headers)

    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    
    playsound("output.mp3",True)
    os.remove("output.mp3")

def Spidy():
    Speech(random.choice(["Bentornato Signor Stark", "Bentornato signore"]))

    r = Recognizer()

    with Microphone() as source:
        print("Pronto ad Ascoltare...")
        
        audio = r.listen(source)
        text = ""
        try:
            text = r.recognize_google(audio, language="it-IT").lower()
        except:
            text = "Error"
        print(text)    
        if "ciao" in text:
            risposta = "Ciao anche a te"
        elif any(parola in text for parola in ["nome", "chiami", "chi sei"]):
            risposta = "Io sono il tuo amichevole Spider-Man di quartiere"
        elif "come stai" in text:
            risposta = "Io sto bene Grazie, e Tu?"
        elif any(parola in text for parola in ["cosa fai", "cosa sai", "che sai"]):
            risposta = "Per ora sono solo in grado di rispondere in maniera programmata alle domande, ma presto sarò aggiornato"
        elif any(parola in text for parola in ["ora", "ore", "orario"]):
            risposta = f"sono le ore {datetime.now().strftime('%H e %M')}"
        else:
            risposta = random.choice(["Scusami, ma non ho capito", "Potresti Ripetere..."])
        
        Speech(risposta)
        