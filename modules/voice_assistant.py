import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import pyttsx3
import datetime

recognizer = sr.Recognizer()
microphone = sr.Microphone()
engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = engine



    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def takeCommand(self):
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")
        with sr.Microphone() as source:
            print("Listening....")
            recognizer.pause_threshold = 1
            # recognizer.energy_threshold = 20
            audio = recognizer.listen(source)
        try:
            print("Recognizing....")
            self.query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return self.query


    def welcome(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speak("good morning")
        elif hour >= 12 and hour < 18:
            self.speak("good afternoon")
        else:
            self.speak("good evening")

        self.speak("Welcome to the multimodal authentication page. First of all, please choose your mode.")
        self.speak("If you want to connect with voice press one, otherwise press two")
        self.speak(
            " In this step, we have to find out you are live. Once you are ready, tell us I am ready to start the procedure")

    def response(self):

        if 'ready' in self.query:
            self.speak('You have chosen the voice communication. At the first step we kindly want you to show the demanded sticker with your hand in front of the camera ')


