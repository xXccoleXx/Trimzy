import os
import speech_recognition as sr
import ffmpeg

command2mp3 = "ffmpeg -i output.mp4 speech.mp3"
command2wav = "ffmpeg -i speech.mp3 speech.wav"
os.system(command2mp3)
os.system(command2wav)
r = sr.Recognizer()
with sr.AudioFile("speech.wav") as source:
     audio = r.record(source, duration=20) 
print(r.recognize_google(audio))