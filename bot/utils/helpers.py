import os
import sys
import yt_dlp
import requests
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
DOWNLOAD_DIR = "downloads"
CLASSPLUS_API_URL = "https://www.classplusapp.com/api"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
}

# Ensure download directory exists
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# Function to download video using yt-dlp
def download_video(url: str):
    try:
        logging.info(f"Starting download for URL: {url}")
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
            'format': 'best',
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        logging.info("Download completed successfully.")
    except Exception as e:
        logging.error(f"Error downloading video: {str(e)}")

# Function to handle Classplus video links
def handle_classplus_link(link: str):
    try:
        logging.info(f"Processing Classplus link: {link}")
        # Extract video ID from the link
        video_id = extract_classplus_video_id(link)
        if not video_id:
            logging.error("Invalid Classplus link. Unable to extract video ID.")
            return

        # Fetch video info from Classplus API
        video_info = fetch_classplus_video_info(video_id)
        if not video_info:
            logging.error("Failed to fetch video information from Classplus API.")
            return

        # Extract video URL and download
        video_url = video_info.get("videoUrl")
        if video_url:
            download_video(video_url)
        else:
            logging.error("No video URL found in the response.")
    except Exception as e:
        logging.error(f"Error handling Classplus link: {str(e)}")

# Helper function to extract video ID from Classplus link
def extract_classplus_video_id(link: str) -> str:
    try:
        # Assuming the video ID is the last part of the URL
        return link.split("/")[-1]
    except Exception as e:
        logging.error(f"Error extracting video ID: {str(e)}")
        return ""

# Helper function to fetch video information from Classplus API
def fetch_classplus_video_info(video_id: str) -> dict:
    try:
        api_url = f"{CLASSPLUS_API_URL}/v1/videos/{video_id}"
        response = requests.get(api_url, headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"API request failed with status code: {response.status_code}")
            return {}
    except Exception as e:
        logging.error(f"Error fetching video info: {str(e)}")
        return {}

# Main function
def main():
    if len(sys.argv) < 2:
        logging.error("Please provide a video link as a command-line argument.")
        sys.exit(1)

    link = sys.argv[1]
    if "classplusapp.com" in link:
        handle_classplus_link(link)
    else:
        download_video(link)

if __name__ == "__main__":
    main()
