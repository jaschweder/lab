package main

import (
	"fmt"
	"sort"
)

func main() {
	list := []int{3, 4, 5, 2, 1}
	
	c := make(chan int)
	
	go func () {
		sort.Sort(sort.IntSlice(list))
		c <- 1
	}()
	
	<-c
	
	fmt.Println(list)
}
