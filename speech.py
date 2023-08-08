"""
Takes in a video and prints out the juicy dialogue.

Author: Chase Coleman
Date: 8/3/2023
"""
import os
import speech_recognition as sr


def get_text(input):
    command2mp3 = f"ffmpeg -i {input}.mp4 speech.mp3"
    command2wav = "ffmpeg -i speech.mp3 speech.wav"
    os.system(command2mp3)
    os.system(command2wav)
    r = sr.Recognizer()
    with sr.AudioFile("speech.wav") as source:
        audio = r.record(source, duration=20) 
        result = r.recognize_google(audio, show_all=True)
        print(result)
    os.remove("speech.mp3")
    os.remove("speech.wav")


get_text("output")