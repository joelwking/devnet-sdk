SANDBOX
-------

These instructions guide you through the process of creating an AWS EC2 instance and optionally automate the installation of Docker CE (Docker Engine - Community package) on the target host. These instructions can be used for setting up a learning environment for DevNet certification study.

A secondary goal of these instructions, is to provide an example of using an Ansible playbook to provision an EC2 instance.

## Create the EC2 instance

Logon the AWS dashboard.

Create a key pair in the AWS console and save on my local Linux system. Change the permissions of the file.

```bash
chmod 600 /home/administrator/amazon_web_service/sdk/devnet_sdk_demo.pem
```
In AWS console, create an EC2 instance, `t2.small` should be sufficient. In testing Ubuntu 16.04 LTS is used.

```
Ubuntu Server 16.04 LTS (HVM), SSD Volume Type - ami-04763b3055de4860b (64-bit x86) / ami-02ca3cadbcb293e21 (64-bit Arm)

```
Associate a security group with the instance permitting HTTP/HTTPS (80/443) and SSH (22).

Connect to AWS instance to verify.

```bash
ssh -i "~/amazon_web_service/sdk/devnet_sdk_demo.pem" ubuntu@ec2-54-208-198-12.compute-1.amazonaws.com
```
Logoff if you are installing Docker via the playbook, otherwise skip to the section on *Installing Docker manually*.

## Install Docker
You can choose to install Docker using an Ansible playbook or via SSH and using the individual commands.

If you would like to automate the deployment of Docker, use the following section. You may wish to review the playbook before execution to familiarize yourself with the tasks. 

### Run Playbook

Add your instance to your inventory, use the `inventory.yml` file in the repository as an example. Many cloud deployments use a dynamic inventory plugin, for this demo, we are only creating one EC2 instance, so we will add the FQDN to the inventory manually.

Download the playbook to your local machine.
```bash
wget https://raw.githubusercontent.com/joelwking/devnet-sdk/master/playbooks/install_docker.yml
```

Review and run the playbook.
```bash
./install_docker.yml --private-key=~/amazon_web_service/sdk/devnet_sdk_demo.pem --user ubuntu
```

The output should look similar to the following.
```
administrator@flint:~/ansible/playbooks$ ./install_docker.yml --private-key=~/amazon_web_service/sdk/devnet_sdk_demo.pem --user ubuntu

PLAY [Install Docker CE on Ubuntu] ****************************************************************************************************************

TASK [Uninstall old versions] *********************************************************************************************************************
ok: [ec2-54-208-198-12.compute-1.amazonaws.com]

TASK [add Docker apt signing key] *****************************************************************************************************************
changed: [ec2-54-208-198-12.compute-1.amazonaws.com] => (item=https://download.docker.com/linux/debian/gpg)

TASK [setup Docker apt repository on Debian] ******************************************************************************************************
changed: [ec2-54-208-198-12.compute-1.amazonaws.com]

TASK [Install packages to allow apt to use a repository over HTTPS] *******************************************************************************
changed: [ec2-54-208-198-12.compute-1.amazonaws.com]

TASK [Install Docker-CE] **************************************************************************************************************************
changed: [ec2-54-208-198-12.compute-1.amazonaws.com]

TASK [Add the user to the Docker group (eliminate the need to run sudo)] **************************************************************************
changed: [ec2-54-208-198-12.compute-1.amazonaws.com]

PLAY RECAP ****************************************************************************************************************************************
ec2-54-208-198-12.compute-1.amazonaws.com : ok=6    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Installing Docker manually

You can choose to install docker manually rather than use the Ansible playbook.

#### Ubuntu (Debian) Docker installation instructions
Add the Docker’s official GPG key:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Use the following command to set up the stable repository. (The below is ONE long line of text)
```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

Update the apt package index.
```bash
sudo apt-get update
```
Install the latest version of Docker CE
```bash
sudo apt-get -y install docker-ce
```
Add the lab login user to the Docker group.
```bash
sudo usermod -aG docker $USER
```
**Important!** Log out and log in again so that your group membership is re-evaluated.

### Verify Docker installation
with either the manual installation, or using the Ansible playbook, Verify that you can run Docker commands without sudo.
```bash
docker run hello-world
```
Now you have installed the Docker CE successfully.

## References

Thanks to the *Cisco AI and ML Training Lab Guide Version v1.3.2* using OS: Ubuntu 16.04 LTS, as a reference in creating student labs in AWS EC2.