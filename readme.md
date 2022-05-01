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

### Deployment

1. For testing and developing locally, you should use  
`
    docker-compose up
`  
in /app to run a Flask server

2. Once your API has been fine-tuned, make adjustments to the  
files in one of the lambda folders, each folder corresponds to a different  
function

3. Use the readme.md instructions to build and test, and run autodeploy.sh  
to automatically deploy to ECR