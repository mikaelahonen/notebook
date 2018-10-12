# Docker notes

## Why to use
For example when using python it takes surprisingly lot of effort to install right versions and packages in each of the environments. With Docker you only have to do the effort of installing the Docker, while everything else is standardized.

## Install
[Install for Windows](https://docs.docker.com/docker-for-windows/install/)

In linux after installation `sudo service docker start`.

## Try Docker
* [Create a docker file](https://docs.docker.com/get-started/part2/#define-a-container-with-dockerfile).
* [Explore docker](https://docs.docker.com/docker-for-windows/#test-your-installation).

## Enable hyper-v
[Enable hyper-v](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v).

After enabling hyper-V and restarting the computer, it might take a while for Docker to launch.

## Processes
Running containers: `docker ps`

[Stop container](https://docs.docker.com/engine/reference/commandline/stop/): `docker stop serene_galileo`
<<<<<<< HEAD

## Images
List images `docker images`.

Remove images not associated with a container: `docker system prune`.

Remove stopped containers and unused images: `docker system prune -a`.

Remove selected images: `docker rmi Image Image`.

## Build
Go to the directory of Dockerfile.

Build `docker build -t mycontainername .`

The image is in computer's Docker image registry.

Run the app `docker run -p 4000:80 mycontainername`.

Visit `http://localhost:4000/` on your browser.

In Windows stop container explicitly `docker container stop <Container NAME or ID>`
=======
>>>>>>> 3457f025b3fa9cbe6ef976106c5538b40f509373
