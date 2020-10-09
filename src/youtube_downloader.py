import youtube_dl as yd
from src.youtube_downloader_logger import YoutubeDownloaderLogger
from src.utils import *
import os

class YoutubeDownloader:
    def __init__(self):
        self.logger = YoutubeDownloaderLogger()
        self.temp_folder = "../temp/"

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

        yd.YoutubeDL(ydl_opts).download([format_video_url(url)])

    def download_and_slice_mp3(self, url: str, directory_path: str = "./", begin: int = 0, end: int = None):
        url = format_video_url(url)
        self.download_mp3(url,"../temp/")
        filename = self.get_id(url)
        music = slice_audio(pd.AudioSegment.from_mp3(f"{self.temp_folder + filename}.mp3"), begin, end)
        music.export(f"{directory_path + filename}.mp3")
        os.remove(self.temp_folder + filename + ".mp3")

    def get_id(self, url: str):
        return self.get_info(url).get("id")

    def get_info(self, url: str):
        ydl_opts = {
            'logger': self.logger,
        }
        return yd.YoutubeDL(ydl_opts).extract_info(url, download=False)
