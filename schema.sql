DROP TABLE IF EXISTS users, topic, category, comments, hearts CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT
);

CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE topic (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users ON DELETE CASCADE,
    title TEXT,
    times TIMESTAMP,
    catid INTEGER REFERENCES category
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users ON DELETE CASCADE,
    topic_id INTEGER REFERENCES topic ON DELETE CASCADE,
    comment TEXT,
    times TIMESTAMP
);

CREATE TABLE hearts (
    acc_id INTEGER REFERENCES users,
    comm_id INTEGER REFERENCES comments ON DELETE CASCADE,
    PRIMARY KEY (acc_id, comm_id)
);

CREATE INDEX ON hearts (comm_id)
;

INSERT INTO category (name) VALUES
('All'),
('Opinion'),
('Question');


