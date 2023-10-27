import os
import pytube
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from pytube.cli import on_progress

def download_as_mp3(url, output_folder, username, password):
    try:
        # Create a YouTube object with login credentials
        yt = YouTube(url, on_progress_callback=on_progress)
        yt.register(username, password)

        # Create a folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Download as mp3
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_filename = os.path.join(output_folder, f"{yt.title}.mp3")
        audio_stream.download(output_path=output_folder, filename=output_filename)

        print(f"Downloaded as mp3: {output_filename}")

    except pytube.exceptions.RegexMatchError:
        print("Invalid YouTube URL.")
    except Exception as e:
        print(f"An error occurred: {e}")

def choose_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    folder_selected = filedialog.askdirectory(title="Select Output Folder")

    if folder_selected:
        return folder_selected
    else:
        return None

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_folder = choose_folder()
    username = input("Enter your YouTube username: ")
    password = input("Enter your YouTube password: ")

    if output_folder:
        download_as_mp3(video_url, output_folder, username, password)

