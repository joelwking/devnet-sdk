DevNet SDK
----------
World Wide Technology, DevNet Associate Study Group

Overview
--------
This repository provides a foundation for exam preparation the Cisco DevNet Associate. The learning material is focused on Software Development Kit (SDKs), Cisco product APIs, the Meraki SDK, and an Introduction to Python.

How to use this learning environment
------------------------------------
Initally we targeted a cloud instance (AWS EC2) to host the Jupyter Notebook. That implementation does not require any software on the student laptop (workstation) other than an SSH client, as Docker is running in the cloud instance.

It has been updated to use Visual Studio Code (a source-code editor made by Microsoft for Windows, Linux and macOS)  and the Docker Dev Container extension and Docker Desktop. 

Presentations
-------------
A companion presentation (initially developed using the cloud instance) for SDK/APIs is available at [https://www.slideshare.net/joelwking/devnet-study-group-using-a-sdk](https://www.slideshare.net/joelwking/devnet-study-group-using-a-sdk).

The presentation developed for the _Introduction to Python_ using the Dev Container is available at [https://www.slideshare.net/joelwking/devnet-associate-python-introduction](https://www.slideshare.net/joelwking/devnet-associate-python-introduction).

Dev Container
-------------
Using the Dev Container eliminates the need to configure and pay for cloud compute resources. Additionally, is is much simplier to get the server up and running quickly. 

Clone this repository `git clone ...` to your local machine. 

Install the required software and the remote container extension on your laptop (workstation).

* Docker Desktop. Download and install Docker Desktop for your target development environment, https://www.docker.com/products/docker-desktop
* Visual Studio Code, [Download and install it](https://code.visualstudio.com/download) and the [Visual Studio Code Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).

Select the 'Extensions' sidebar menu item and enter `remote` in the Search Extensions in Marketplace dialog box and install this extension (ms-vscode-remote.remote-containers).

You can also locate and install the [Visual Studio Code Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) from the web link.

> Note: You may need to restart VS code after installing the Extension Pack for the extension to be recognized.

From VS Code, issue a `File -> Open Workspace`, and select the `workspace.code-workspace` in this directory and follow the prompts to build the Docker image and container. Once complete, you can open a terminal window, enable the Python virtual environment, `source /opt/jupyter/bin/activate`. Run `jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root` to start the notebook service. Copy the URL specified in the standard output from the `jupyter notebook` command. Substitute the host port mapped for port `8888`. 

Using a web browser, paste the specified URL, using the host port assigned and open the notebook file(s) of interest.

Cloud Instance
--------------
In the root directory, `SANDBOX.md`  provides instructions on creating an AWS EC2 instance and installing Docker CE, either manually or using the Ansible playbook `playbooks/install_docker.yml`.

In the `library/notebooks` directory, `README.md` provides instructions on how to install and run the Docker image specified in `library/notebooks/Dockerfile`. The running container is used to execute an instance of **Jupyter notebooks**.  Within the container, Python3, the Meraki SDK, a sample notebook (`library/notebooks/Using_a_SDK.ipynb`) and Python program (`library/notebooks/using_meraki_sdk.py`) are referenced in the lab guide `library/notebooks/MERAKI_README.md`.

There is a notebook showing an implementation of  rate limiting logic to address any *429* errors. Refer to the notebook under `library/notebooks/Meraki_Rate_Limiting_example.ipynb`.

Author
------
joel.king@wwt.com (@joelwking)
