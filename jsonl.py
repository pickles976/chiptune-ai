import json
import os
from random import randint

INDIR = "./NES_ABC"
KEYS_JSON = "signatures.json"

keys = {}

with open(KEYS_JSON,"r") as f:
    keys = json.load(f)

# print(keys)

files = os.listdir(INDIR)

completions = ""
songnum = 0

# offset removing boilerplate
offset = 33

for key in keys:

    songs = keys[key]

    for song in songs:

        fn = os.path.join(INDIR,song)

        with open(fn,"r") as songfile:

            data = songfile.read()

            tokens = data.split(" ")
            numtokens = len(tokens)

            beginning = [data[:offset]]

            # make sure our songs are of a decent length
            if numtokens < 2048 and numtokens > 256:

                entry = {"prompt" : key,
                    "completion" : " " + data[offset:]} # whitespace character helps training

                completions += json.dumps(entry) + "\n"
                songnum += 1

print(f"Completions file contains {songnum} songs!")

with open("completions.jsonl","w") as f:
    f.write(completions)

# files = os.listdir(INDIR)

# print(f"There are {len(files)} files!")

# completions = ""
# songnum = 0

# # offset removing boilerplate
# offset = 33

# for f in files:

#     if f.split(".")[1] == "abc":

#         fn = os.path.join(INDIR,f)

#         with open(fn,"r") as songfile:

#             data = songfile.read()

#             tokens = data.split(" ")
#             numtokens = len(tokens)

#             beginning = [data[:offset]]

#             # make sure our songs are of a decent length
#             if numtokens < 2048 and numtokens > 256:

#                 entry = {"prompt" : f"{randint(0,9999):04d}",
#                     "completion" : " " + data[offset:]} # whitespace character helps training

#                 completions += json.dumps(entry) + "\n"
#                 songnum += 1


# print(f"Completions file contains {songnum} songs!")

# with open("completions.jsonl","w") as f:
#     f.write(completions)
