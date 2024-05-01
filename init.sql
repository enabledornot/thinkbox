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
CREATE OR REPLACE FUNCTION detect_spam()
RETURNS TRIGGER AS $$
DECLARE
    recent_uuid uuid;
    recent_time TIMESTAMP;
BEGIN
    IF TG_OP = 'INSERT' THEN
        SELECT s_id, time INTO recent_uuid, recent_time FROM comments ORDER BY time DESC LIMIT 1;
        IF NEW.s_id = recent_uuid AND EXTRACT(EPOCH FROM (NEW.time - recent_time)) < 300 THEN
            RAISE EXCEPTION 'spam_like_behavior_detected';
        END IF;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER prevent_spam
BEFORE INSERT ON comments
FOR EACH ROW
EXECUTE FUNCTION detect_spam();