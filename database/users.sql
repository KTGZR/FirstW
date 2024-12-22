CREATE TABLE IF NOT EXISTS users(
    userid SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS holidays(
    userid SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO users(email,password) VALUES
('proverka@mail.ru','proverka'),('q@mail.ru','12345');
