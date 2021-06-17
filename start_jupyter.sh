#!/usr/bin/env bash
#
#      Copyright (c) 2021 World Wide Technology
#      All rights reserved.
#
#      author: @joelwking
#
#      description: 
#        Run Jupyter in the Python venv configured for this project
#
source /opt/jupyter/bin/activate
echo 'you are executing in ('`basename $VIRTUAL_ENV`')'
jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root