import re


""" Extract all of the midi file names from the database
"""

BASE_URL = "https://www.vgmusic.com/music/console/nintendo/nes/"

results = []
href = "<a[^>]+href=\"(.*?)\"[^>]*>(.*)?</a>"

# open webpage
with open("nes.txt","r") as myFile:

    # loop through the HTML 
    for line in myFile:
        text = re.findall(href,line) # extract all lines with href
        if len(text) > 0 and len(text[0]) > 1: # extract and check for midi files
            mid = text[0][0]
            spl = mid.split(".")
            if len(spl) > 1 and spl[1] == "mid":
                results.append(mid)

outfile = "NES_URL.txt"

with open(outfile,"w") as out:

    for url in results:
        out.write(BASE_URL + url + "\n")

