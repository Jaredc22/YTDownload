import os
from yt_dlp import YoutubeDL

def download_youtube(url, audio_only=False, resolution="1080", download_path=None):
    """
    Download a YouTube video or audio file.
    Args:
        url (str): YouTube video URL
        audio_only (bool): If True, downloads as MP3
        resolution (str): Max resolution (e.g., "1080", "720")
        download_path (str): Folder path for saving output
    Returns:
        str: Message about result or error
    """
    if not url:
        return "❌ No URL provided."

    if not download_path:
        download_path = os.path.expanduser("~/Downloads")
    os.makedirs(download_path, exist_ok=True)

    common_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'ffmpeg_location': '/opt/homebrew/bin/ffmpeg',  # adjust if needed
        'quiet': True,
    }

    if audio_only:
        ydl_opts = {
            **common_opts,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        ydl_opts = {
            **common_opts,
            'format': f"bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]/best",
            'merge_output_format': 'mp4',
        }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "✅ Download complete!"
    except Exception as e:
        return f"❌ Error: {e}"