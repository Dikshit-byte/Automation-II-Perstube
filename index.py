from operator import index
from pytube import YouTube,Playlist
import pprint
from pytube import Search
from pytube.cli import on_progress

# yt = YouTube("https://youtu.be/pJZ9tT8OwFk")
# p = Playlist("https://youtube.com/playlist?list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2")
# p.download()
# print(yt.title)
# print(yt.thumbnail_url)
# print(yt.age_restricted)
# print(yt.author)
# print(yt.length)
# print(str(yt.description))
# print(yt.streams)

fuchsia = '\033[38;2;255;00;255m'   #  color as hex #FF00FF
reset_color = '\033[39m'

s = Search(input("Enter your search : "))
print(s.results[0])
videoID = s.results[0].video_id
print(s.results[0].video_id)
print(s.get_next_results())

yt1 = YouTube("https://youtu.be/"+videoID,on_progress_callback=on_progress)
print(yt1.title)
# yt1.streams.filter(only_audio=True).first().download()
# print(yt1.streams)
print(yt1.captions)
# yt1.streams.filter(file_extension='mp4').get_highest_resolution().download()
print(f'\n' + fuchsia + 'Downloading: ',yt1.title, '~ viewed', yt1.views, 'times.')
yt1.streams.filter(file_extension='mp4').get_lowest_resolution().download()
print(f'\nFinished downloading:  {yt1.title}' + reset_color)
