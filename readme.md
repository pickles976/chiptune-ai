https://github.com/chrisdonahue/nesmdb#midi-format

- GAN
https://www.youtube.com/watch?v=T-MCludVNn4

- MIDI2IMG
https://github.com/mathigatti/midi2img

### Getting the data

1. Run the utility to get the URLs      
` 
    python .\Utilities.py getUrls [BASE_URL] [IN_FILE] [OUT_FILE]
`   
2. Run downloader.py to get all of the Midi files   
`
    python .\Utilities.py downloadMidis [OUT_DIR] [URLS_FILE]
`   

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
4. Run removetracks to remove all non-standardized tracks          
    `   
        python .\Utilities.py removeTracks [IN_DIR]
    `
5. Run jsonl.py to create jsonl training file from abc files    
    `
        python .\Utilities.py jsonl [IN_DIR] [OUT_FILE]
    `

### Training

1. Run this command to further prep the training file:     
`
    openai tools fine_tunes.prepare_data -f .\completions.jsonl 
`
2. Run the training     
`
    openai api fine_tunes.create -t .\completions_prepared.jsonl -m curie
`