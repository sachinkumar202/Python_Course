import moviepy.editor

from tkinter.filedialog import *

vid = askopenfilename()
video = moviepy.editor.VideoFileClip(vid)

aud = video.audio
aud.write_audiofile("demp.mp3")

print("---End---")
