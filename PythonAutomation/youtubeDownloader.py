from pytube import YouTube
from sys import argv
import pathlib

link = argv[1] #takes the arguments (the video) from the command line
yt = YouTube(link)

# video information
print(yt.title)
print(yt.views)

# Download the video
yd = yt.streams.get_highest_resolution()
applicationPath = pathlib.Path().resolve()
yd.download(applicationPath)