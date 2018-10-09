package main

import (
	"fmt"

	"github.com/gocql/gocql"
	"github.com/scylladb/gocqlx"
	"github.com/scylladb/gocqlx/qb"
)

type Person struct {
	FirstName string
	LastName  string
	Email     []string
}

var exampleKeyspace = `
CREATE KEYSPACE example
	WITH REPLICATION = {
		'class': 'SimpleStrategy',
		'replication_factor': 1
	};
`

var personSchema = `
	CREATE TABLE IF NOT EXISTS example.person(
		first_name text,
		last_name text,
		email list<text>,
		PRIMARY KEY(first_name, last_name)
	)
`

func main() {
	cluster := gocql.NewCluster("db")
	cluster.Keyspace = "example"
	cluster.Consistency = gocql.Quorum
	session, err := cluster.CreateSession()

	if err != nil {
		panic(err)
	}

	// C - Create
	p := &Person{
		"John",
		"Doe",
		[]string{"john@doe.com"},
	}

	stmt, names := qb.Insert("person").
		Columns("first_name", "last_name", "email").
		ToCql()

	q := gocqlx.Query(session.Query(stmt), names).BindStruct(p)

	if err := q.ExecRelease(); err != nil {
		panic(err)
	}

	fmt.Printf("%s created\n", p.FirstName)

	// R - Read One

	stmt, names = qb.Select("person").
		Where(qb.Eq("first_name")).
		ToCql()

	q = gocqlx.Query(session.Query(stmt), names).BindMap(qb.M{
		"first_name": "John",
	})

	var john Person
	if err = gocqlx.Get(&john, q.Query); err != nil {
		panic(err)
	}

	fmt.Printf("%s was found\n", john.FirstName)

	// R - Read All

	stmt, names = qb.Select("person").
		Where(qb.Eq("first_name")).
		ToCql()

	q = gocqlx.Query(session.Query(stmt), names).BindMap(qb.M{
		"first_name": "John",
	})

	var people []Person
	if err = gocqlx.Select(&people, q.Query); err != nil {
		panic(err)
	}

	fmt.Printf("%d total people found\n", len(people))

	// U - Update

	p.Email = append(p.Email, "doe@john.com")

	stmt, names = qb.Update("person").
		Set("email").
		Where(qb.Eq("first_name"), qb.Eq("last_name")).
		ToCql()

	q = gocqlx.Query(session.Query(stmt), names).BindStruct(p)

	if err := q.ExecRelease(); err != nil {
		panic(err)
	}

	fmt.Println("Added 'doe@john.com' email")

	// D - Delete

	stmt, names = qb.Delete("person").
		Where(qb.Eq("first_name"), qb.Eq("last_name")).
		ToCql()

	q = gocqlx.Query(session.Query(stmt), names).BindStruct(p)

	if err := q.ExecRelease(); err != nil {
		panic(err)
	}

	fmt.Printf("Deleted %s %s\n", p.FirstName, p.LastName)
}
