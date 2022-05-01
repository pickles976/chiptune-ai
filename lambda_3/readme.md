Lambda function for getting new completions for a given song

To build and reploy, run autodeploy.sh

Test locally:
docker build -t midi-shuffle .
docker run -p 9000:8080 midi-shuffle
POST "http://localhost:9000/2015-03-31/functions/function/invocations"