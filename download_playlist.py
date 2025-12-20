import os
from pytube import Playlist
import re

# 1. Paste the URL of the Apna College DSA Playlist here
# Example structure (replace with actual URL):
PLAYLIST_URL = "https://youtube.com/playlist?list=PLGjplNEQ1it-OKRcYlCEDpTiIB1YOcvn6&si=IMV0zQOsGVmIxCp6" 

# 2. Define the output folder where your RAG data lives
DOWNLOAD_DIR = r"D:\Python Projects\RAG Based AI Teaching Assistant\Course_Videos"

# Create the directory if it doesn't exist
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)
    print(f"Created directory: {DOWNLOAD_DIR}")

try:
    # Create a Playlist object
    playlist = Playlist("https://youtube.com/playlist?list=PLGjplNEQ1it-OKRcYlCEDpTiIB1YOcvn6&si=IMV0zQOsGVmIxCp6")

    # This is a good practice to handle playlist parsing errors in pytube
    # You may or may not need this line depending on the pytube version:
    # playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    print(f"Starting download for playlist: {playlist.title}")
    print(f"Total videos to download: {len(playlist.video_urls)}")

    for index, video in enumerate(playlist.videos, start=1):
        print(f"\n--- Downloading Video {index}/{len(playlist.video_urls)} ---")

        # Filter for a progressive stream (video + audio combined, usually MP4)
        # and select the best resolution available
        stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if stream:
            # Download the file to the specified directory
            stream.download(output_path=DOWNLOAD_DIR, filename_prefix=f"{index:02d}_")
            print(f"✅ Downloaded: {video.title}")
        else:
            print(f"❌ Could not find a suitable stream for: {video.title}")

except Exception as e:
    print(f"An error occurred: {e}")

print("\n\nAll downloads complete!")