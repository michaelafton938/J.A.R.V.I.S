import pyttsx3
import pyaudio
import speech_recognition

engine = pyttsx3.init()
engine.setProperty("voice", "french")
engine.setProperty("rate", 100)
engine.say("Initialisation du système J.A.R.V.I.S")
engine.say("Initialisation du système J.A.R.V.I.S terminé" )
engine.say ("Que puis-je faire pour vous monsieur")

from speech_recognition import Recognizer, Microphone

recognizer = Recognizer()

# On enregistre le son

with Microphone() as source:

    print("Réglage du bruit ambiant... Patientez...")
    recognizer.adjust_for_ambient_noise(source)
    print("Vous pouvez parler...")
    recorded_audio = recognizer.listen(source)
    print("Enregistrement terminé")
# Reconnaissance de l'audio

try:
    print("Reconnaissance du texte...")
    text = recognizer.recognize_google(
        recorded_audio,
        language="fr-FR"
    )
    print("Vous avez dit : {}".format(text))

except Exception as ex:
    print(ex)