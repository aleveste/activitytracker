CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    laji TEXT,
    kesto TEXT,
    extra TEXT,
    sent_at TIMESTAMP
);
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    group_name TEXT UNIQUE,
    group_info TEXT,
    owner_id INTEGER REFERENCES users
);
CREATE TABLE groupmembers (
    group_id INTEGER REFERENCES groups,
    member_id INTEGER REFERENCES users
);
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    event_name TEXT UNIQUE,
    event_info TEXT,
    organizer_id INTEGER REFERENCES users
);
CREATE TABLE eventmembers (
    event_id INTEGER REFERENCES events,
    member_id INTEGER REFERENCES users
);
CREATE TABLE admins (
    id SERIAL PRIMARY KEY,
    user_id INTEGER
);