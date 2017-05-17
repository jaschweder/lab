package main

import(
    "log"
    "fmt"

    "github.com/gocql/gocql"
)

func main() {
    cluster := gocql.NewCluster("db")
    cluster.Keyspace = "question"
    cluster.Consistency = gocql.One
    session, _ := cluster.CreateSession()

    // create
    if err := session.Query(`INSERT INTO questions(question, response) VALUES (?, ?)`,
        "tchau", "tchau").Exec(); err != nil {
            log.Fatal(err)
    }

    var question string;
    var response string;

    // retrieve one
    if err := session.Query(`SELECT question, response FROM questions LIMIT 1`).Scan(&question, &response); err != nil {
            log.Fatal(err)
    }
    fmt.Println("Question: ", question, response)

    // retrieve many
    iter := session.Query(`SELECT question, response FROM questions`).Iter()
    for iter.Scan(&question, &response) {
        fmt.Println("Question: ", question, response)
    }
    if err := iter.Close(); err != nil {
        log.Fatal(err)
    }

    // update
    if err := session.Query(`UPDATE questions SET response = ? WHERE question = ?`,
        "tchau", "oi").Exec(); err != nil {
            log.Fatal(err)
    }

    // delete
    if err := session.Query(`DELETE FROM questions WHERE question = ?`,
        "oi").Exec(); err != nil {
            log.Fatal(err)
    }

    session.Close()
}
