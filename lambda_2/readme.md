Lambda function for generating a new song from scratch

docker build -t midi-gen .

Test locally:
docker run -p 9000:8080 midi-gen
POST "http://localhost:9000/2015-03-31/functions/function/invocations"