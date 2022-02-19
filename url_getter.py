import re


""" Extract all of the midi file names from the database
"""

BASE_URL = "https://www.vgmusic.com/music/console/nintendo/nes/"
INPUT_FILE = "nes.txt"
OUTPUT_FILE = "NES_URL.txt"

results = []
href = "<a[^>]+href=\"(.*?)\"[^>]*>(.*)?</a>"

# open webpage
with open(INPUT_FILE,"r") as myFile:

    # loop through the HTML 
    for line in myFile:
        text = re.findall(href,line) # extract all lines with href
        if len(text) > 0 and len(text[0]) > 1: # extract and check for midi files
            mid = text[0][0]
            spl = mid.split(".")
            if len(spl) > 1 and spl[1] == "mid":
                results.append(mid)

with open(OUTPUT_FILE,"w") as out:

    for url in results:
        out.write(BASE_URL + url + "\n")

