# Linux commands

## Search file

## Install python 3.6 on Ubuntu

[Tutorial for Ubuntu 16](http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/). In Ubuntu 18 python 3.6 should be pre-installed. Try it with command `python3 -V`.

**Install python 3.6**

sudo add-apt-repository ppa:jonathonf/python-3.6

sudo apt-get update

sudo apt-get install python3.6

**Select version**

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2

sudo update-alternatives --config python3

**Show version**

python3 -V

## Install pip for Ubuntu

[Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-18-04-quickstart)

sudo apt update

sudo apt install python3-pip

sudo apt install -y python3-pip

After this python packages can be installed by
`pip3 install package_name`

## Install docker on Ubuntu 18.04 Windows Subsystem

[Tutorial](https://medium.com/@sebagomez/installing-the-docker-client-on-ubuntus-windows-subsystem-for-linux-612b392a44c4)
