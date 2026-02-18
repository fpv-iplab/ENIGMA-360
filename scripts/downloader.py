import argparse
import os
import requests
import zipfile
import tarfile
from io import BytesIO

# --- Configuration ---
BASE_URL = "https://iplab.dmi.unict.it/ENIGMA-360/data"
SPLIT_REPO_URL = "https://raw.githubusercontent.com/user/repo/main/splits"

def download_file(url, dest_path):
    """Downloads a file to the specified path."""
    print(f"Downloading: {url}")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    else:
        print(f"Failed to download {url} (Status: {response.status_code})")
        raise FileNotFoundError()


def main():
    parser = argparse.ArgumentParser(description="Dataset Downloader")
    
    # Flags
    parser.add_argument("--splits", nargs="+", choices=["train", "test", "val"], default=["train"],
                        help="Select splits to download (e.g., --splits train val)")
    parser.add_argument("--mode", choices=["videos", "frames"], required=True,
                        help="Download raw videos or extracted frames")
    parser.add_argument("--view", choices=["ego", "exo", "both"], default="both",
                        help="Camera perspective")
    
    args = parser.parse_args()
    output_dir = "data"

    ids = []
    for split in args.splits:
        print(f"--- Processing {split} split ---")
        # 1. Fetch split file from GitHub (Mock logic)
        # split_url = f"{SPLIT_REPO_URL}/{split}.txt"
        with open(f"annotations/{split}.txt", 'r') as splitf:
            ids = splitf.readlines()
        
        for vid in ids:
            views_to_download = ["ego", "exo"] if args.view == "both" else [args.view]
            
            for view in views_to_download:
                if args.mode == "videos":
                    suffix = "first_person" if view == "ego" else "third_person"
                    url = f"{BASE_URL}/videos/{vid}/{vid}_{suffix}.mp4"
                    dest = os.path.join(output_dir, args.mode, vid, f"{vid}_{suffix}.mp4")
                    download_file(url, dest)
                
                else: # Frames mode
                    # This assumes a naming convention for frames (e.g., 001.jpg)
                    # Realistically, you'd loop through a frame index or list
                    counter = 1
                    while True:
                        try:
                            frame_url = f"{BASE_URL}/frames/{view}/{vid}/{vid}_{counter:010d}.jpg"
                            dest = os.path.join(output_dir, args.mode, view, vid, f"{vid}_{counter:010d}.jpg")
                            download_file(frame_url, dest)
                            counter += 1
                        except:
                            break


if __name__ == "__main__":
    main()