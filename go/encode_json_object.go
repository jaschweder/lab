package main

import (
	"encoding/json"
	"os"
)

type Person struct {
	Name string `json:"name"`
}

type People []Person

func main() {
	p := new(Person)
	p.Name = "John Doe"
	
	encoder := json.NewEncoder(os.Stdout)
	encoder.Encode(p)
}
