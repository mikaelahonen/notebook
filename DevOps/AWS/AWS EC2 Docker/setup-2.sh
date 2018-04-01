#!/bin/sh
docker info
docker build -t web-app .
docker images --filter reference=web-app
#Run the app in default http port
docker run -p 80:80 web-app
