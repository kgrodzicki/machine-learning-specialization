# machine-learning-specialization

Use  [graphlab-create-docker](https://github.com/flow-lab/graphlab-create-docker) to build docker image with graphlab-create included.  Best to use graphlab-create license version 2.1. Older versions cannot be longer obtained in python repositories like pip.
After successful build navigate to machine-learning-specialization repository and run docker image: 
```
$ docker run --rm -it -p 8888:8888 -v "$(shell pwd):/notebooks" flowlab/graphlab-create
```

Open jupyter notebook in your browser http://DOCKER_IP:8888, eg. http://192.168.99.100:8888 and browse the examples.
