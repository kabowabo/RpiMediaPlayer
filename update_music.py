from yt_dlp import YoutubeDL

playlist_url = "https://music.youtube.com/playlist?list=PLwtmDkaE16Q16z1QKG0EB1jRiq1BKin33&si=9ksRp34DdgqSsuQM"
output_dir = "/home/sumedh/mediaplayer/music"

options = {
    'format': 'bestaudio/best',
    'outtmpl': f'{output_dir}/%(playlist_index)s - %(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'download_archive': f'{output_dir}/downloaded.txt',  # skip existing
    'quiet': True,
}

with YoutubeDL(options) as ydl:
    ydl.download([playlist_url])

