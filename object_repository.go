package main

import (
	"encoding/json"
	"os"
)

const (
	QUERY_RESULT_LIMIT = 30
)

type Person struct {
	Name string `json:"name"`
}

type People []Person

type PersonRepository struct {}

func (r *PersonRepository) Get() (People) {
	p1 := new(Person)
	p1.Name = "John Doe"
	
	p2 := new(Person)
	p2.Name = "Mary Doe"
	
	people := People{}
	people = append(people, *p1)
	people = append(people, *p2)
	
	if len(people) > QUERY_RESULT_LIMIT {
		panic("Return has unespected lenght")
	}
	
	return people
}

func main() {
	encoder := json.NewEncoder(os.Stdout)
	personRepository := new(PersonRepository)
	var people People = personRepository.Get()
	encoder.Encode(people)
}
