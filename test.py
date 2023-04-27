import yt_dlp as youtube_dl # client to many multimedia portals

# downloads yt_url to the same directory from which the script runs
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'thatfile.mp3',
}
abc = "https://www.youtube.com/watch?v=gedYii6S_0c"
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([abc])

