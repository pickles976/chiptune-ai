https://docs.aws.amazon.com/lambda/latest/dg/images-create.html
https://console.aws.amazon.com/ecr/repositories?region=us-east-1

docker build -t midi-api .   

docker tag  531418479922.dkr.ecr.us-east-1.amazonaws.com/midi-api
docker push 531418479922.dkr.ecr.us-east-1.amazonaws.com/midi-api         
aws ecr get-login-password | docker login --username AWS --password-stdin 531418479922.dkr.ecr.us-east-1.amazonaws.com/midi-api 

aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 531418479922.dkr.ecr.us-east-2.amazonaws.com    
aws ecr create-repository --repository-name midi-api --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
docker tag  midi-api:latest 531418479922.dkr.ecr.us-east-2.amazonaws.com/midi-api
docker push 531418479922.dkr.ecr.us-east-2.amazonaws.com/midi-api:latest  