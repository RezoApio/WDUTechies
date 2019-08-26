# Useful docker commands

## Checking running container 
docker ps -a

## Checking images 
docker image ls

## Building images from Dockerfile
mkdir WDUbuntu
cd WDUbuntu
vi Dockerfile
docker build -t wdubuntu .

## Running the container
docker run -it -d wdubuntu /bin/bash