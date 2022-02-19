https://www.vgmusic.com/music/console/nintendo/nes/mariotheme.mid

### Getting the data

1. Run the utility to get the URLs      
` 
    python .\Utilities.py getUrls [BASE_URL] [IN_FILE] [OUT_FILE]
`   
2. Run downloader.py to get all of the Midi files   
`
    python .\Utilities.py downloadMidis [OUT_DIR] [URLS_FILE]
`   
3. Run normalization steps:
    - Normalize the track numbers   
    `
        python .\Utilities.py normalizeTracks [IN_DIR]
    `   
4. Convert all of the midi -> XML -> abc files      
`
    python .\Utilities.py midi2abc [IN_DIR] [OUT_DIR]
`   
5. Run purge.py to remove all of the XML files      
`
    python .\Utilities.py purgeXML [IN_DIR]
`   
6. Run jsonl.py to create jsonl training file from abc files    
`
    python .\Utilities.py jsonl [IN_DIR] [JSON_KEYS] [OUT_FILE]
`

### Training

1. Run this command to further prep the training file:     
`
    openai tools fine_tunes.prepare_data -f .\completions.jsonl 
`
2. Run the training