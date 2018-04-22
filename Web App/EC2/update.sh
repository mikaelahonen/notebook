#!/bin/sh
docker stop web-app
docker build -t web-app .
#Run the app in default http port
docker run -p 8001:8001 web-app
