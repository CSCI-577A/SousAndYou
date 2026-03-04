This README is for developers only

Starting the docker image for local testing of caching
prereq - download docker for desktop

docker run --name localhost -p 6379:6379 -d redis

Start backend
prereq - pip install -r requirements.txt
python3 flask_api.py

Start up EC2 Instance to communicate with Claude - this should already be running. Check before running the next steps
Save pem file locally
ssh into ec2 instance: ssh -i "~\ec2-577a.pem" ec2-user@ec2-35-164-2-29.us-west-2.compute.amazonaws.com
cd backend
python3 app.py

