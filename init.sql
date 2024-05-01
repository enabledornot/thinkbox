CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE IF NOT EXISTS sessions (
    s_id uuid PRIMARY KEY,
    create_date TIMESTAMP
);
CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    s_id uuid,
    author VARCHAR(32) NOT NULL,
    time TIMESTAMP,
    text VARCHAR(8192) NOT NULL,
    user_agent VARCHAR(512),
    FOREIGN KEY (s_id) REFERENCES sessions(s_id)
);