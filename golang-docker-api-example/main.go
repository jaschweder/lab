package main

import (
    "log"
    "bytes"

	"github.com/docker/docker/api/types"
	"github.com/docker/docker/api/types/container"
	"github.com/docker/docker/client"
	"golang.org/x/net/context"
)

func listContainers() ([]types.Container) {
	cli, err := client.NewEnvClient()
	if err != nil {
		panic(err)
	}

    containers, err := cli.ContainerList(context.Background(), types.ContainerListOptions{})
    if err != nil {
        panic(err)
    }

    return containers
}

func removeContainer(id string) {
	cli, err := client.NewEnvClient()
	if err != nil {
		panic(err)
	}

    cli.ContainerRemove(context.Background(), id, types.ContainerRemoveOptions{})
}

func runContainer(img string, cmd []string, wait bool) (id, output string) {
	ctx := context.Background()
	cli, err := client.NewEnvClient()
	if err != nil {
		panic(err)
	}

	out, err := cli.ImagePull(ctx, img, types.ImagePullOptions{})
	if err != nil {
		panic(err)
	}

	resp, err := cli.ContainerCreate(ctx, &container.Config{
		Image: img,
		Cmd:   cmd,
		Tty:   true,
	}, nil, nil, "")
	if err != nil {
		panic(err)
	}

	if err := cli.ContainerStart(ctx, resp.ID, types.ContainerStartOptions{}); err != nil {
		panic(err)
	}

    if wait == false {
        return resp.ID, ""
    }

    defer removeContainer(resp.ID)

	_, err = cli.ContainerWait(ctx, resp.ID)

    if err != nil {
        panic(err)
    }

	out, err = cli.ContainerLogs(ctx, resp.ID, types.ContainerLogsOptions{ShowStdout: true})
	if err != nil {
		panic(err)
	}

    buf := new(bytes.Buffer)
    buf.ReadFrom(out)
    return resp.ID, buf.String()
}

func main() {
    //id, out := runContainer("jaschweder/php", []string{"php", "--version"}, true)
    //log.Println("Container ID:", id)
    //log.Println("Output: ", out)
    var containers []types.Container = listContainers()
    for _, c := range containers {
        log.Println(c.Image)
    }
}
