### Example of how to use Docker SDK in Golang

#### Getting started

Install dependencies using [dep](https://github.com/golang/dep)

```sh
$ dep ensure
```

Run inside docker container

```sh
$ docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock -v $PWD:/go/src/github.com/jaschweder/golang-docker-api golang bash
```

See `main.go` file to see more details
