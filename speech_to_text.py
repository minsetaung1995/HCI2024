# speech_to_text.py
import speech_recognition as sr

def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return "I'm sorry, I didn't catch that."
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return "I'm having trouble connecting to the speech service."
