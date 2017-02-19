Title: Dockerizing a Website
Date: 2014-12-18 20:30
Slug: dockerizing
Status: Draft

Docker is a platform for developing, shipping, and running applications using container technology.

Hypervisor is a thing that allows you to install multiple vms with their own systems on one server.

VMs allow to conveniently run several things on one server, but VMs require their own operating systems.

**Container** uses the kernel of the operating system, but has it's own filesystem, memory, devices, ports, etc.

**Image** is a read only template used to build a container. Stored on docker hub.
**Docker Engine** (deamon) is a program that allows me to build, ship, and run containers.

It uses some namespaces, dunno what they are. That's okay.

# Install
Install docker on ubuntu:
https://docs.docker.com/engine/installation/linux/ubuntulinux/

sudo docker run hello-world

## Add user to the docker group so that you wouldn't have to use sudo
sudo usermod -aG docker ray

## Docker start demon
sudo service docker start

## Docker run
Take an image, create a container out of it, and run that container
docker run <image>
To give it a name instead of weird code:
docker run --name web1 <image>

-d will run it in the background.

## Docker start/stop
Start/stop an existing image
docker start <name|id>
docker stop <name|id>

## Docker list containers
List running containers:
docker ps
Include stopped containers:
docker ps -a

## Delete container
docker rm  <name|id>

## Login
docker login
to log into the docker hub, the repository of containers, like github
docker run containername
and it will just run it!!

## Expose port
That will connect container's port to the server's port, so that anybody could access it.
docker run -p 8080:80
(first one is the server port, and the second one is the docker port)


so basically you want:
docker run -d --name nexus -p 80:80 rayalez/nexus
# Resources
Great official getting started course:
https://training.docker.com/introduction-to-docker
Medium article:
https://medium.freecodecamp.com/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b
One more great post:
https://serversforhackers.com/getting-started-with-docker

Mastodon deployment tutorial:
https://github.com/Gargron/mastodon

Great short tutorial on docker and DO:
https://www.youtube.com/watch?v=JBtWxj9l7zM

# Install
