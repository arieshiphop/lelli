from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
from config import config as c
import commands as cmd
import platform
r = sr.Recognizer()
class TTS:
    def __init__(self,language):
        self.lang = language

    def speak(self,text):
        """
        This method will speak the text you pass to it
        """
        tts = gTTS(text, lang=self.lang)
        tts.save('voice.mp3')
        playsound('voice.mp3')
        os.remove('voice.mp3')

    def listen(self):
        """
        This method will listen for commands\n
        All commands are in commands.py\n
        All the bot responses are configured on config.py
        """
        with sr.Microphone() as source:
            self.speak(c['possible_answers']["listening"])
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                self.speak((c['possible_answers']['said']+" "+text))
                self.read_command(text)
                
            except:
                self.speak(c['voice_errors']['bad_voice'])

                self.listen()
    def read_command(self,text):
        text = text.lower()
        "Here you can add your commands detected on listen()"
        if "exit" in text:
            cmd.exit()
        if "open google" in text:
            cmd.open_google()
        if "open youtube" in text:
            cmd.open_youtube()
        if "joke" in text:
            self.speak(c['possible_answers']['laugh'])
        if "computer" in text:
            cmd.system_info(self)
tts = TTS(c['langs']['English'])
tts.read_command("computer")