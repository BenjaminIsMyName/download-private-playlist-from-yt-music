from songs import songs
from yt_dlp import YoutubeDL


urls = [song.split("&")[0] for song in songs if "watch" in song]

params = {"format": "bestaudio", "outtmpl": "songs/%(title)s.%(ext)s"}
with YoutubeDL(params) as ydl:
    ydl.download(urls)
