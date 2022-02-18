https://www.vgmusic.com/music/console/nintendo/nes/mariotheme.mid

1. Run url_getter.py on an HTML text document to extract all the midi URLs
2. Run downloader.py to get all of the Midi files
3. Run midi2abc.py to convert all of the midi -> XML -> abc files
4. Run purge.py to remove all of the XML files
5. Run jsonl.py to create jsonl training file from abc files