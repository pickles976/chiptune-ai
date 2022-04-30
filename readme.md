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
5. Upload folders to Google Drive and run the Colab to create datasets   
    `
        https://colab.research.google.com/drive/1Qex7hxW-FCpxNJOZXUY0My83dqUHn7T3
    `  
    This step needs to be updated with a dedicated notebook

### Training

https://colab.research.google.com/drive/1N8m1dL71Tj138g0NFbG32DcGLA9cYVoK