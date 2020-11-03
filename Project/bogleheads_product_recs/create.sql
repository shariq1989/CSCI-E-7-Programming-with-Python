CREATE TABLE threads(
	id 		SERIAL 	PRIMARY KEY,
	thread_id	INT NOT NULL,
	thread_title	TEXT
);

CREATE TABLE links(
	id 		SERIAL	PRIMARY KEY,
	url		TEXT NOT NULL,
	date_posted	DATE,
	author		TEXT,
	thread_id	INT REFERENCES threads(id),
	post_number	INT
);