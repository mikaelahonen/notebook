#!/bin/sh
sudo yum update -y
sudo yum install -y docker
sudo service docker start
#Add the ec2-user to the docker group
#to execute Docker commands without using sudo
sudo usermod -a -G docker ec2-user
