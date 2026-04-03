CREATE DATABASE IF NOT EXISTS hellmusic
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE hellmusic;

CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY,
    user_name VARCHAR(255) DEFAULT '',
    join_date VARCHAR(50) DEFAULT '',
    songs_played INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS chats (
    chat_id BIGINT PRIMARY KEY,
    join_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS auth_chats (
    chat_id BIGINT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS auth_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chat_id BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    user_name VARCHAR(255) DEFAULT '',
    auth_by_id BIGINT DEFAULT 0,
    auth_by_name VARCHAR(255) DEFAULT '',
    auth_date VARCHAR(50) DEFAULT '',
    UNIQUE KEY uq_chat_user (chat_id, user_id)
);

CREATE TABLE IF NOT EXISTS autoend (
    id INT PRIMARY KEY DEFAULT 1,
    enabled TINYINT(1) DEFAULT 0
);

CREATE TABLE IF NOT EXISTS blocked_users (
    user_id BIGINT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS gban_users (
    user_id BIGINT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS sudo_users (
    user_id BIGINT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS favorites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    video_id VARCHAR(100) NOT NULL,
    title VARCHAR(500) DEFAULT '',
    duration VARCHAR(50) DEFAULT '',
    add_date VARCHAR(50) DEFAULT '',
    UNIQUE KEY uq_user_video (user_id, video_id)
);

CREATE TABLE IF NOT EXISTS songs_counter (
    id INT PRIMARY KEY DEFAULT 1,
    count INT DEFAULT 0
);

INSERT IGNORE INTO autoend (id, enabled) VALUES (1, 0);
INSERT IGNORE INTO songs_counter (id, count) VALUES (1, 0);
