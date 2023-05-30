from songs import songs
import subprocess


urls = [song.split("&")[0] for song in songs if "watch" in song]

for url in urls:
    # subprocess.run(["yt-dlp", "-f", "bestaudio", url])
    # or download into the "songs" folder instead of the current directory:
    subprocess.run(["yt-dlp", "-f", "bestaudio", "-o", "songs/%(title)s.%(ext)s", url])
