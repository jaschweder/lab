# Installation

```sh
$ docker run -d --name scylladb -v $PWD:/dump scylladb/scylla --memory 1G
$ docker run -it --rm --name go-scylla -v $PWD:/go golang bash
```
