https://www.vgmusic.com/music/console/nintendo/nes/mariotheme.mid

1. Run url_getter.py on an HTML text document to extract all the midi URLs
2. Run downloader.py to get all of the Midi files
3. Run normalization steps:
    - normalizer.py to normalize the track numbers
    - run getkeys.py to extract key signatures from songs
4. Run midi2abc.py to convert all of the midi -> XML -> abc files
5. Run purge.py to remove all of the XML files
6. Run jsonl.py to create jsonl training file from abc files
7. Run this command to further prep the training file:     
`
    openai tools fine_tunes.prepare_data -f .\completions.jsonl 
`
8. Run the training