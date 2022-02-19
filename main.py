import subprocess


musicfile = "4.txt"
songname = musicfile.split(".")[0]
out = songname + ".abc"

boilerplate = """X:1
T:Music21 Fragment
C:Music21 \n"""

music = ""

with open(musicfile,"r") as f:
    music += boilerplate

    data = f.read().split("\\n")

    for line in data:
        music += line + "\n"

with open(out,"w") as f:
    f.write(music)

