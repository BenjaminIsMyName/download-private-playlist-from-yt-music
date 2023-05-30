from songs import songs
import subprocess
from yt_dlp import YoutubeDL


urls = [song.split("&")[0] for song in songs if "watch" in song]

for url in urls:
    # OPTION 1: use subprocess.run
    # subprocess.run(["yt-dlp", "-f", "bestaudio", url])
    # OPTION 2: or download into the "songs" folder instead of the current directory:
    # subprocess.run(["yt-dlp", "-f", "bestaudio", "-o", "songs/%(title)s.%(ext)s", url])
    # OPTION 3: or use the YoutubeDL class:
    # with YoutubeDL() as ydl:
    #     ydl.download(urls)
    # OPTION 4: or download into the "songs" folder instead of the current directory:
    # with YoutubeDL({"outtmpl": "songs/%(title)s.%(ext)s"}) as ydl:
    #     ydl.download(urls)
    # OPTION 5: specify "bestaudio" format:
    params = {"format": "bestaudio", "outtmpl": "songs/%(title)s.%(ext)s"}
    with YoutubeDL(params) as ydl:
        ydl.download(urls)
