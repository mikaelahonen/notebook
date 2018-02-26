## Build
Go to the directory of Dockerfile.

Build `docker build -t friendlyhello .`

The image is in computer's Docker image registry.

Run the app `docker run -p 4000:80 friendlyhello`

In Windows stop container explicitly `docker container stop <Container NAME or ID>`