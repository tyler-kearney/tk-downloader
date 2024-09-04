import tkinter as tk
from tkinter import ttk
import requests
import tqdm as tqdm
import os
import shutil

# defining the function to manage the download logic
def file_download():
    url = url_entry.get()
    response = requests.get(url, stream=True)
    
    total_size = int(response, response.headers.get("content-length", 0))
    
    with open("downloaded_file.zip", "wb") as f, tqdm(total=total_size, unit="B", unit_scale=True, desc=url) as p:
        for data in response.iter_content(chunk_size=1024):
            size = len(data)
            f.write(data)
            p.update(size)
            
    # move the downloaded file to the downloads folder
    shutil.move("downloaded_file.zip", os.path.join(os.path.expanduser("~"), "Downloads"))

# Creating the window for the UI
# Create the main window
window = tk.Tk()

# Input field and download button
in_label = tk.Label(window, text="Download URL: ")
in_label.pack()

url_entry = tk.Entry(window)
url_entry.pack()

download_btn = tk.Button(window, text="Download", command=file_download)
download_btn.pack()

# Create the progress bar
progress_bar = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
progress_bar.pack()

window.mainloop()