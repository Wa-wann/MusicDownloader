import youtube_dl as yd
from src.youtube_downloader_logger import YoutubeDownloaderLogger


class YoutubeDownloader:
    def __init__(self):
        self.logger = YoutubeDownloaderLogger()

    def download_mp3(self, url: str, directory_path: str = "./"):
        ydl_opts = {
            'format': 'bestaudio',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }, ],
            'outtmpl': f"{directory_path}%(id)s.%(ext)s",
            'logger': self.logger,
        }

        yd.YoutubeDL(ydl_opts).download([url])
