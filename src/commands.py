import os
import webbrowser
import platform


def open_youtube():
    webbrowser.open("https://www.youtube.com/")
def exit():
    os._exit(0)
def open_google():
    webbrowser.open("https://www.google.com/")
def system_info(tts):
    tts.speak("Windows version: "+platform.platform())
    tts.speak("Processor: "+platform.processor())
    tts.speak("System: "+platform.system())
    tts.speak("Machine: "+platform.machine())
    tts.speak("System version: "+platform.version())
