#
#     Copyright (c) 2021 World Wide Technology
#     All rights reserved.
#
#     author: joel.king@wwt.com
#     written:  1 June 2021
#     references:
#       activate virtualenv: https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
#       https://github.com/wwt/network-endpoint-mapper
#
FROM python:3.8.10-slim-buster
ENV VIRTUAL_ENV=/opt/jupyter
LABEL maintainer="Joel W. King" email="joel.king@wwt.com"
RUN apt update && \
    apt -y install git && \
    apt -y install python3-venv && \
    pip3 install --upgrade pip 
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#
# We need the requirements.txt for installation
#
RUN mkdir /src
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt
#
#  source /opt/jupyter/bin/activate
#  jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root
#
