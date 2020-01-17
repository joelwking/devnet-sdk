README
------

## Install and run the Docker image

Log on your assigned account on the EC2 instance.

```bash
ssh -i "~/amazon_web_service/sdk/devnet_sdk_demo.pem" ubuntu@ec2-54-208-198-12.compute-1.amazonaws.com
```

In addition to the AWS security group configuration which allows TCP ports 80, 442 and 22, update the host firewall to allow inbound connections to map to the container port(s). Assuming we expose port 80, update the firewall configuration.

```bash
sudo ufw allow http
```
Clone the repository into the home directory.
```bash
git clone https://github.com/joelwking/devnet-sdk.git
```
Enter the library directory
```bash
cd ~/devnet-sdk/library
```

Build the Docker image.
```bash
docker build -f ./notebooks/Dockerfile -t  joelwking/meraki:0.9 .

```
You should see the final output indicating that the image was successfully built and tagged.
```bash
 docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
joelwking/meraki    0.9                 05c5fc4940f3        23 seconds ago      576MB
ubuntu              latest              ccc6e87d482b        39 hours ago        64.2MB
```

Run the image, creating a container with the working directory mapped to the host file system.
```bash
docker run -it --name meraki -p 80:8888 --volume /home/ubuntu/devnet-sdk/library/notebooks:/src/notebooks joelwking/meraki:0.9
```

You will be attached to the Bash shell of the container.
```bash
root@ed5d2a4d1812:/src/notebooks#
```
The working directory of the container is mapped to the host file system. Verify this by tailing the `Dockerfile` used to create the image.
```bash
cat Dockerfile
```
Review the contents of the Dockerfile The Docker container has Jupyter installed. 

## Start Jupyter notebooks.

```bash
root@ed5d2a4d1812:/src/notebooks# jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root
```
The notebook console displays the token needed to connect to the web interface. Also note how to exit the notebook server.
```bash
[I 16:51:49.481 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[I 16:51:49.737 NotebookApp] Serving notebooks from local directory: /src/notebooks
[I 16:51:49.738 NotebookApp] The Jupyter Notebook is running at:
[I 16:51:49.738 NotebookApp] http://ed5d2a4d1812:8888/?token=9cad1f32d110d43b999ccdb56fe7dc0bed32ccf89df3fead
[I 16:51:49.738 NotebookApp]  or http://127.0.0.1:8888/?token=9cad1f32d110d43b999ccdb56fe7dc0bed32ccf89df3fead
[I 16:51:49.739 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 16:51:49.744 NotebookApp] No web browser found: could not locate runnable browser.
[C 16:51:49.744 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/nbserver-15-open.html
    Or copy and paste one of these URLs:
        http://ed5d2a4d1812:8888/?token=9cad1f32d110d43b999ccdb56fe7dc0bed32ccf89df3fead
     or http://127.0.0.1:8888/?token=9cad1f32d110d43b999ccdb56fe7dc0bed32ccf89df3fead

```
From your laptop, connect to the EC2 instance on port 80 and specifiy the token provided in the console output. For example.
```
http://ec2-54-208-198-12.compute-1.amazonaws.com:80/?token=9cad1f32d110d43b999ccdb56fe7dc0bed32ccf89df3fead
```
You should be presented with the main Jupyter screen. The URL in your browser will look similar to: [http://ec2-54-208-198-12.compute-1.amazonaws.com/tree](http://ec2-54-208-198-12.compute-1.amazonaws.com/tree)

## Create a new notebook
In the upper right size of the screen, select NEW -> Python 3. You will be presented with an Untitled notebook. Click on Untitled, Enter a new notebook name. Click on the floppy drive icon to Save and Checkpoint, or File -> Save and Checkpoint.

On the console you should see information messages like:
```
[I 18:55:59.478 NotebookApp] Saving file at /Using_a_SDK.ipynb
```
Congratulations, You have Jupyter Notebooks running in a Docker container in the cloud!

## Exiting 
From the container console, you can se Control-C to stop this server and shut down all kernels. You can exit the container by issuing CTL + p + q.

Because the container files system and the host are mapped to each other, the notebook you recently saved is present.

```bash
root@ed5d2a4d1812:/src/notebooks# ls *.ipynb
Using_a_SDK.ipynb
```
If you view the file, note that the notebook contents is simply a JSON file. For example.

```bash
cat Using_a_SDK.ipynb
```
**WARNING**: If you enter credentials into the notebook, they will be present in clear text. Be careful with the contents of the notebook descriptor file.

To again attach to the running container, locate the container name or ID and issue the *docker attach* command.

```bash
$ docker ps
CONTAINER ID        IMAGE                  COMMAND             CREATED             STATUS              PORTS                  NAMES
ed5d2a4d1812        joelwking/meraki:0.9   "/bin/bash"         2 hours ago         Up 2 hours          0.0.0.0:80->8888/tcp   meraki
ubuntu@ip-172-31-44-75:~$
```

```bash
docker attach meraki
```
Because you exited the application, you will need to restart, see *Start Jupyter notebooks* above.