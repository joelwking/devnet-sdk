# devnet-sdk
World Wide Technology, DevNet Associate Study Group, **Using a SDK**.

## Overview
The engineers at World Wide Technology have formed a DevNet study group. This repository is the foundation for the DevNet certification exam study group on the topic of Software Development Kit (SDKs) and APIs.  This collateral is used for exam preparation the Cisco DevNet Associate certification.

This repository provides instructions, a sample Ansible playbook, a Dockerfile, and sample Jupyter notebooks to create a learning environment on using the Meraki SDK and other Cisco product APIs. 

## Presentation
The companion presentation for this repository is available at [https://www.slideshare.net/joelwking/devnet-study-group-using-a-sdk](https://www.slideshare.net/joelwking/devnet-study-group-using-a-sdk).

## Demo environment
The examples can be executed using a cloud instance (like AWS EC2), or by using VS CODE and a Dev Container.

### Dev Container
The preferred method is to use VS Code and a Dev Container. When using this method, clone this repository to your local machine. Use these steps and install the required software and the remote container extension.

* Docker Desktop. Download and install Docker Desktop for your target development environment, https://www.docker.com/products/docker-desktop
* Visual Studio Code, [Download and install it](https://code.visualstudio.com/download) and the [Visual Studio Code Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).

Select the 'Extensions' sidebar menu item and enter `remote` in the Search Extensions in Marketplace dialog box and install this extension (ms-vscode-remote.remote-containers).

You can also locate and install the [Visual Studio Code Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) from the web link.

> Note: You may need to restart VS code after installing the Extension Pack for the extension to be recognized.

From VS Code, issue a `File -> Open Workspace`, and select the `workspace.code-workspace` in this directory and follow the prompts to build the Docker image and container. Once complete, you can open a terminal window and run `jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root` to start the notebook service. Copy the URL specified in the standard output from the `jupyter notebook` command. Substitute the host port mapped for port `8888`. 

Using a web browser, paste the specified URL and open the notebook you wish to examine.

### Cloud Instance
In the root directory, `SANDBOX.md`  provides instructions on creating an AWS EC2 instance and installing Docker CE, either manually or using the Ansible playbook `playbooks/install_docker.yml`.

In the `library/notebooks` directory, `README.md` provides instructions on how to install and run the Docker image specified in `library/notebooks/Dockerfile`. The running container is used to execute an instance of **Jupyter notebooks**.  Within the container, Python 3, the Meraki SDK, a sample notebook (`library/notebooks/Using_a_SDK.ipynb`) and Python program (`library/notebooks/using_meraki_sdk.py`) are referenced in the lab guide `library/notebooks/MERAKI_README.md`.

Additionally, content has been added to include a notebook which walks the student through implementing rate limiting logic to address any *429* errors. Refer to the notebook under `library/notebooks/Meraki_Rate_Limiting_example.ipynb`.

## Cultural Aside
In addition to using the environment for learning how to use the Meraki SDK, Cloud computing instances running Docker and Jupyter notebooks are common for big data analytics and machine learning. Do a web search on *"why ai/ml use docker and jupyter notebooks"* - you will find a number of references to this combination of tools for AI/ML projects.

## Author
joel.king@wwt.com (@joelwking)
