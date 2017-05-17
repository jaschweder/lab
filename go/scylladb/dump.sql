CREATE KEYSPACE question
  WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE question;

CREATE TABLE questions (
    question text PRIMARY KEY,
    response text
);
