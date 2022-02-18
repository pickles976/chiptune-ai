import os

OUTDIR = "./NES_ABC"

for f in os.listdir(OUTDIR):
    if f.split(".")[1] == "musicxml":
        print(f"Removing file: {f}")
        os.remove(os.path.join(OUTDIR,f))