CREATE TABLE IF NOT EXISTS users(
    userid SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL UNIQUE
);

INSERT INTO users(email,password) VALUES
('proverka@mail.ru','proverka'),('q@mail.ru','12345');

CREATE TABLE IF NOT EXISTS lastupdate(
    tableid SERIAL PRIMARY KEY,
    tablename VARCHAR(255) NOT NULL UNIQUE,
    updatedate TIMESTAMP
)

CREATE TABLE IF NOT EXISTS holidays(
    userid SERIAL PRIMARY KEY,
)