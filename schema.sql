DROP TABLE IF EXISTS todos;

CREATE TABLE todos (
	"id" integer PRIMARY KEY,
	"description" varchar(140),
	"status" boolean,
	"created_date" timestamp DEFAULT (now())::timestamp(0) without time zone
);


