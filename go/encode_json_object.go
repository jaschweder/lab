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
	p1 := new(Person)
	p1.Name = "John Doe"
	
	encoder := json.NewEncoder(os.Stdout)
	encoder.Encode(p1)
	
	p2 := new(Person)
	p2.Name = "Mary Doe"
	
	people := People{}
	people = append(people, *p1)
	people = append(people, *p2)
	encoder.Encode(people)
}
