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
CREATE TABLE follows (
    id SERIAL PRIMARY KEY,
    follower_id INTEGER REFERENCES users,
    followed_id INTEGER REFERENCES users
);
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    group_name TEXT,
    group_info TEXT,
    owner_id INTEGER REFERENCES users
);
CREATE TABLE groupmembers (
    group_id INTEGER REFERENCES groups,
    member_id INTEGER REFERENCES users
);
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    event_name TEXT,
    event_info TEXT,
    organizer_id INTEGER REFERENCES users
);
CREATE TABLE eventmembers (
    event_id INTEGER REFERENCES events,
    member_id INTEGER REFERENCES users
);