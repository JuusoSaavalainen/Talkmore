CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
);

CREATE TABLE topic (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users,
    title TEXT,
    visible INTEGER
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users,
    topic_id INTEGER REFERENCES topic,
    comment TEXT
);


