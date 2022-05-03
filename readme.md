# [Chiptune.app](https://www.chiptune.app)

This is a project for creating NES-like chiptune music using Natural Language Processing. This includes the data collection, normalization, and model training-- as well as a Dockerfile for locally developing and testing different generation functions with Flask.

The front-end is available [here](https://github.com/pickles976/chiptune-react)

Special thanks to [Max Woolf](https://github.com/minimaxir) for creating [aitextgen](https://github.com/minimaxir/aitextgen), which was much easier to configure and use than raw HuggingFace transformers.

A majority of my data is from the [LAKH_MIDI dataset](https://colinraffel.com/projects/lmd/) which contains ~170k MIDI files. Also special thank you to [Chris Donahue](https://github.com/chrisdonahue) and the [LAKH_NES project](https://github.com/chrisdonahue/LakhNES) which I used for guidance throughout this project.

# Running The Server

## Deployment

1. Copy [this folder](https://drive.google.com/drive/folders/14Jv8KSieuQgUrQ6q-YUiqxPdkc9i9QcT?usp=sharing) into the app/model/ folder.  
Rename it to "GPT_NEO"

2. Run
`
    docker-compose up
`  
in /app to run a Flask server. If it is your first time building then it will take a hot minute.


# Making your own model

## Getting the data

1. Navigate to a page like:  
`
    http://www.vgmusic.com/music/console/nintendo/snes/  
`  
Copy the source HTML of the page to a file

2. Run the utility to get the URLs from the HTML (could be automated, base URL is URL from previous step)
` 
    python .\Utilities.py getUrls [BASE_URL] [IN_FILE] [OUT_FILE]
`   

3. Run downloader.py to get all of the Midi files   
`
    python .\Utilities.py downloadMidis [OUT_DIR] [URLS_FILE]
`   

(note: all of the data is already in /data_scraping)

## Pre-Processing

1. Run normalization steps:
    - Normalize the track numbers   
    `
        python .\Utilities.py normalizeTracks [IN_DIR]
    `   
2. Convert all of the midi -> XML -> abc files      
    `
        python .\Utilities.py midi2abc [IN_DIR] [OUT_DIR]
    `   
3. Run purge.py to remove all of the XML files      
    `
        python .\Utilities.py purgeXML [IN_DIR]
    `   
5. Create datasets of appropriate length  
    a. Upload your folder of .abc files to Google drive  
    b. Open huggingface_train.ipynb in Google Colab  
    c. Run the commands until your dataset is generated  
    d. Save your dataset locally  
    (note: sufficiently large datasets will need to be manually saved
    with utf-8 encoding, as they will be created with ANSI encoding by default)

## Training

1. Open up aitextgen_training.ipynb in Google Colab  
2. Either train from scratch (this will generate a new model and tokenizeer) or--
3. Continue training (Finetune)
4. Once training is done, move your model into the /model/ folder in /app
