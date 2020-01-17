#
#     Copyright (c) 2020 World Wide Technology, LLC
#     All rights reserved.
#
#     author: joel.king@wwt.com (@joelwking)
#     written:  14 January 2020
#
#     usage:
#
#       from directory `devnet-sdk/library`
#       docker build -f ./meraki/Dockerfile -t  joelwking/meraki:0.9 .
#       docker run -it --name meraki -p 80:8888 --volume /home/ubuntu/src/meraki/notebooks:/src/notebooks joelwking/meraki:0.9
#
#     reference: https://u.group/thinking/how-to-put-jupyter-notebooks-in-a-dockerfile/

FROM ubuntu:latest
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.7 python3-pip python3-dev
#
#  Install the Merkai SDK for our demo
#
RUN pip3 install meraki-sdk
#
#  Add any additional libraries required for the demo
#
RUN pip3 install requests
RUN pip3 install pyyaml
#
# Install Jupyter
#
RUN pip3 install jupyter
#
#  Create base directory
#
RUN mkdir -p /src
#
#  Create subdirectory to store Jupyter Notebooks
#
RUN mkdir -p /src/notebooks
WORKDIR /src/notebooks
#
#  Install Phantom SDK
#
ADD https://raw.githubusercontent.com/joelwking/Phantom-Cyber/master/REST_ingest/PhantomIngest.py /src/notebooks/PhantomIngest.py
#
#  TODO: for the time being, we will start via the shell inside the container
#
# jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root
#
# CMD ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--allow-root"]
