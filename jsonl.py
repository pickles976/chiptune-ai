import json
import os
from random import randint

INDIR = "./NES_ABC"
files = os.listdir(INDIR)

print(f"There are {len(files)} files!")

completions = []

for f in files:

    if f.split(".")[1] == "abc":

        fn = os.path.join(INDIR,f)

        with open(fn,"r") as songfile:

            data = songfile.read()

            tokens = data.split(" ")
            numtokens = len(tokens)

            if numtokens < 2048:

                entry = {"prompt" : f"{randint(0,1000):04d}",
                    "completion" : data }

                completions.append(entry)

print(f"Completions file contains {len(completions)} songs!")

with open("completions.json","w") as f:
    json.dump(completions,f)
