-- Active: 1681613524932@@127.0.0.1@3306@passmanager

CREATE TABLE
    users (
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        site VARCHAR(255) NOT NULL,
        salt VARCHAR(255) NOT NULL,
        CONSTRAINT unique_username_site UNIQUE (username, site)
    );

SELECT * FROM users;