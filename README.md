Docker image with Jupyter Notebook and Graplab Create included. Extending jupyter/notebook - https://github.com/jupyter/notebook.

## Requirements
* Install Docker - https://www.docker.com
* Get your own GraphLab-Create-License.tar.gz file - https://dato.com/products/create/

## Clone the project
```
$ git clone git@github.com:kgrodzicki/machine-learning-specialization.git
```

## Place your own license file in Docker directory
```
$ cd Docker 
$ cp PATH_TO_LICENSE_FILE/GraphLab-Create-License.tar.gz .
```

## Build docker image on your machine
```
$ make build 
```

## Run jupyter notebook
```
$ make run
[I 22:27:18.506 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[W 22:27:18.548 NotebookApp] ipywidgets package not installed.  Widgets are unavailable.
[W 22:27:18.553 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
[W 22:27:18.553 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using authentication. This is highly insecure and not recommended.
[I 22:27:18.573 NotebookApp] Serving notebooks from local directory: /notebooks
[I 22:27:18.573 NotebookApp] 0 active kernels 
[I 22:27:18.573 NotebookApp] The Jupyter Notebook is running at: http://[all ip addresses on your system]:8888/
[I 22:27:18.573 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 22:27:18.574 NotebookApp] No web browser found: could not locate runnable browser.
```

Open jupyter notebook in your browser http://DOCKER_IP:8888, eg. http://192.168.99.100:8888
