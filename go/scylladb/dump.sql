CREATE KEYSPACE example
  WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };

USE example;

CREATE TABLE tweet (
    timeline varchar,
    id varchar PRIMARY KEY,
    text text
);
