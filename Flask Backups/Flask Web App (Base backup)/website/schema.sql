DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id# NUMBER(10),
    firstname VARCHAR2(15) NOT NULL,
    email VARCHAR2(30) NOT NULL,
    password VARCHAR2(7) NOT NULL
);