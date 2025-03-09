import subprocess
from typing import List
import pandas as pd
import csv
from datetime import datetime
current_time = datetime.now().strftime("%Y%m%d_%H%M")
import os
print(os.getcwd())

myNewList = []

def get_channel_video_ids(channel_url: str) -> List[str]:
    """
    Extract all video IDs from a YouTube channel URL using yt-dlp command line.
    
    Args:
        channel_url (str): URL of the YouTube channel
        
    Returns:
        list: List of video IDs from the channel
    """
    try:
        # Run yt-dlp command and capture output 
        result = subprocess.run([
            'yt-dlp',
            '--flat-playlist',
            '--get-id',
            channel_url
        ], capture_output=True, text=True, check=True)
        print(result)
        # Split the output into lines and remove empty lines
        video_ids = [line.strip() for line in result.stdout.split('\n') if line.strip()]
        df = pd.DataFrame(data={"VIDEO_IDs": video_ids})
        df.to_csv(fr"C:\Users\evlo8\Documents\PythonLocal\Get file size of all vids of a channel_builds upon dir 'py_YT-DLP'\test_{current_time}.csv", sep=',', index=False)

        print(f"Total videos found: {len(video_ids)}")
        return video_ids

    except subprocess.CalledProcessError as e:
        print(f"Error running yt-dlp: {e.stderr}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return []


# Example usage
if __name__ == "__main__":
    channel_url = "https://www.youtube.com/@ThePPseedsShow"
    video_ids = get_channel_video_ids(channel_url)
    
    # Print all video IDs
    # print(video_ids)
    # for i, video_id in enumerate(video_ids, 1):
    #     print(f"{i}. {video_id}")

#iterate over list (print iteration) -> Extract transcripts to new files

videoSizeList = []

script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)

for idx, i in enumerate(video_ids):
    # print(idx, i)
    # NB! This does not work! will be -1 less of total video IDs
        # Fixed it! (with "+ 1" after idx)
    print("Video number " + (str(idx + 1)) +" out of " + (str(len(video_ids))))
    try:
        subprocess.run([
            'yt-dlp',
            '-P',
            r"E:\ppshow_archive",
            '-o',
            '%(upload_date>%Y-%m-%d)s %(title)+.100U [%(id)s]',
            f"https://www.youtube.com/watch?v={i}",
        ], cwd=script_dir)
    except:
        pass
