import requests
import os

OUTDIR = "./NES_MIDI"
URL_FILE = "NES_URL.txt"

def download_file(url):

    songname = url.split('/')[-1]
    local_filename = os.path.join(OUTDIR,songname)
    files = os.listdir(OUTDIR)
    if songname not in files:

        print(f"Downloading item #{len(files)}")
        
        # NOTE the stream=True parameter below
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk: 
                    f.write(chunk)
        return local_filename

with open(URL_FILE,"r") as myFile:

    for line in myFile:
        download_file(line.replace("\n",""))

print("Downloads complete!")
