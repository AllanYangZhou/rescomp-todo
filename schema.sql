DROP TABLE IF EXISTS todos;

CREATE TABLE todos (
	"id" integer PRIMARY KEY AUTOINCREMENT,
	"description" varchar(140),
	"status" boolean DEFAULT 0,
	"created_date" timestamp DEFAULT CURRENT_TIMESTAMP
);


