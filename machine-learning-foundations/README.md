## Build docker image
```
$ docker build -t kgrodzicki/mls .
```

## Run in terminal python console
```
$ docker run -it --rm --name mls kgrodzicki/mls
```

## Run container in detached mode
```
$ docker run -it --name mls -d kgrodzicki/mls
```

## Execute ipython in terminal
```
$ docker exec -i -t mls ipython
```
