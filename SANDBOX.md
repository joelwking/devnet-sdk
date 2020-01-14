README
------

In AWS console, create an instance.

t2.small


Connect to AWS instance

 ssh -i "csr1000v/aws_csr1000v.pem" ubuntu@ec2-3-85-88-62.compute-1.amazonaws.com

 or

 ssh -i "csr1000v/aws_csr1000v.pem" ubuntu@3.85.88.62


Add the Docker’s official GPG key:

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Use the following command to set up the stable repository. (The below is ONE long line of text)

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

Update the apt package index.

sudo apt-get update


Install the latest version of Docker CE

sudo apt-get -y install docker-ce


Verify that the Docker CE is installed correctly by running the hello-world image.

sudo docker run hello-world


Add the lab login user to the Docker group.

sudo usermod -aG docker $USER

Log out and log in again so that your group membership is re-evaluated.

Verify that you can run Docker commands without sudo.

docker run hello-world

Now you have installed the Docker CE successfully.


Install and run Docker Image

docker run -it -p 8888:8888 tensorflow/tensorflow:1.10.0

https://u.group/thinking/how-to-put-jupyter-notebooks-in-a-dockerfile/

Be certain of the security groups. The host running the demo and the Phantom VM need to be in the same group