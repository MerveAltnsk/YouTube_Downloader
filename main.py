import yt_dlp

url = input("Enter YouTube URL: ")

try:
    ydl_opts = {
        'format': 'best',  # Select the best available format with video+audio
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download completed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
