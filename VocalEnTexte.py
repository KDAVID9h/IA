import speech_recognition as sr

# Créer un objet de reconnaissance vocale
recognizer = sr.Recognizer()

# Enregistrer l'audio depuis le microphone
with sr.Microphone() as source:
    print("Dites quelque chose...")
    audio = recognizer.listen(source)

# Reconnaître la parole à partir de l'audio
try:
    text = recognizer.recognize_google(audio, language="fr-FR")
    print("Vous avez dit :", text)
except sr.UnknownValueError:
    print("Impossible de reconnaître la parole")
except sr.RequestError as e:
    print("Erreur lors de la requête au service de reconnaissance vocale ; {0}".format(e))
