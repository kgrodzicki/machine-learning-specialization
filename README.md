# machine-learning-specialization

Use  [graphlab-create-docker](https://github.com/flow-lab/graphlab-create-docker) to build docker image with graphlab-create included.  Best to use graphlab-create license version 2.1. Older versions cannot be longer obtained from python repositories like pip.
After successful build navigate to machine-learning-specialization repository and run docker image: 
```
$ docker run --rm -it -p 8888:8888 -v "$(pwd):/notebooks" flowlab/graphlab-create
```
or start script provided 
```
$ ./graplab-create.sh 
[I 19:23:03.996 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[I 19:23:04.051 NotebookApp] Serving notebooks from local directory: /notebooks
[I 19:23:04.052 NotebookApp] 0 active kernels 
[I 19:23:04.052 NotebookApp] The Jupyter Notebook is running at: http://0.0.0.0:8888/
[I 19:23:04.052 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

Open jupyter notebook in your browser http://DOCKER_IP:8888, eg. http://192.168.99.100:8888 and browse the examples.
