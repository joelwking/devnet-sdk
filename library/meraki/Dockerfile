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
#       docker run -it --name meraki -p 80:8888 joelwking/meraki:0.9
#
#     reference: https://u.group/thinking/how-to-put-jupyter-notebooks-in-a-dockerfile/

FROM ubuntu:latest
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev

RUN mkdir -p /src
WORKDIR src/
#
# COPY ./hello_phantom/* /src/
# COPY ./connector/*.py /src/
#
# Install the Merkai SDK for our demo
#
RUN pip3 install meraki-sdk
#
#  Add any additional libraries
#
RUN pip3 install requests
ADD https://raw.githubusercontent.com/joelwking/Phantom-Cyber/master/REST_ingest/PhantomIngest.py /src/PhantomIngest.py
#
#
#
WORKDIR /src/notebooks
#
#
#
RUN pip3 install jupyter

# CMD ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--allow-root"]
