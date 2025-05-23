import os
import subprocess
from typing import List


class YouTubeDownloader:
    def __init__(self, source_file: str, download_folder: str = "downloads"):
        """
        Initialize the downloader.

        :param source_file: Path to the text file containing YouTube links.
        :param download_folder: Folder where videos will be saved.
        """
        self.source_file = source_file
        self.download_folder = download_folder
        os.makedirs(self.download_folder, exist_ok=True)

    def read_links(self) -> List[str]:
        """
        Read all video links from the text file.

        :return: List of YouTube URLs.
        """
        try:
            with open(self.source_file, "r", encoding="utf-8") as file:
                links = [line.strip() for line in file if line.strip()]
            print(f"Found {len(links)} links.")
            return links
        except FileNotFoundError:
            print(f"Error: File not found - {self.source_file}")
            return []

    def download_video(self, url: str):
        """
        Download a single YouTube video using yt-dlp.

        :param url: YouTube video URL.
        """
        try:
            print(f"Downloading: {url}")
            subprocess.run(
                ["yt-dlp", "-P", self.download_folder, url],
                check=True
            )
            print("Downloaded successfully!\n")
        except subprocess.CalledProcessError as e:
            print(f"Failed to download {url} - Error: {e}")

    def download_all(self):
        """
        Download all videos listed in the text file.
        """
        links = self.read_links()
        if not links:
            print("No links found in the file.")
            return

        for link in links:
            self.download_video(link)


if __name__ == "__main__":
    print("Starting the YouTube downloader...")
    downloader = YouTubeDownloader("malie_songs_to_vibe_to/link_video.txt", download_folder="my_videos")
    downloader.download_all()
