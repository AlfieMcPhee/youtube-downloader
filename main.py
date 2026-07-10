from pytubefix import YouTube
from sys import argv

link = argv[1]
youtube = YouTube(link)

print("Title:",youtube.title)
print("Views:",youtube.views)

youtubeDownload = youtube.streams.get_highest_resolution()
youtubeDownload.download()
