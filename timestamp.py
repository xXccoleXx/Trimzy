"""
Uses google cloud speech for advanced options.

Author: Chase Coleman
Date: 8/3/2023
"""

import whisper
model = whisper.load_model("base")
audio = whisper.load_audio("Recording.mp3")
result = model.transcribe(audio)
data = []
for segments in result["segments"]:
    midpoint = (int(segments["end"]) + int(segments["start"]))/2
    data.append((midpoint, segments["text"]))

print(data)
