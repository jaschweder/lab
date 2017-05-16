package main

import(
    "log"
    "fmt"

    "github.com/gocql/gocql"
)

func main() {
    cluster := gocql.NewCluster("db")
    cluster.Keyspace = "example"
    cluster.Consistency = gocql.One
    session, _ := cluster.CreateSession()
    defer session.Close()

    // create
    /*if err := session.Query(`INSERT INTO tweet (timeline, id, text) VALUES (?, ?, ?)`,
        "me", "123", "hello world").Exec(); err != nil {
            log.Fatal(err)
    }*/

    // retrieve
    var id string;
    var text string;
    if err := session.Query(`SELECT id, text FROM tweet WHERE timeline = ? LIMIT 1`,
        "me").Scan(&id, &text); err != nil {
            log.Fatal(err)
    }
    fmt.Println("Tweet: ", id, text)

    // update

    // delete
}
