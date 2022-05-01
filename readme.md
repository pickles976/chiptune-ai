This is a project for creating NES-like chiptune music using  
Natural Language Processing. This includes the data collection, normalization,  
and model training-- as well as containers for locally developing and testing  
different generation functions with Flask, and locally developing and testing  
containers configured for AWS Lambda.


### Getting the data

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

### Pre-Processing

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


### Training

1. Open up aitextgen_training.ipynb in Google Colab  
2. Either train from scratch (this will generate a new model and tokenizeer) or--
3. Continue training (Finetune)
4. Once training is done, move your model into the /model/ folder in /app

### Deployment

1. For testing and developing locally, you should use  
`
    docker-compose up
`  
in /app to run a Flask server