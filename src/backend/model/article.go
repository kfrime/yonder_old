package model

import (
	"database/sql"
	"fmt"
	"time"
)

type Article struct {
	Id 			uint32
	AuthorId 	uint32
	TopicId 	uint32
	Title 		string
	created 	time.Duration
	updated 	time.Duration
}

func tableCreateArticle(db *sql.DB) {
	cmd := `
	create table if not exists t_article (
		id integer not null auto_increment,
		author_id integer not null,
		topic_id integer not null,
		title varchar(100) not null comment 'article title',
		created timestamp not null default current_timestamp,
		updated timestamp not null default current_timestamp on update current_timestamp,
		primary key (id),
		index index_author_id (author_id),
		index index_topic_id (topic_id)
	) engine=InnoDB default charset=utf8mb4;`

	if _, err := db.Exec(cmd); err != nil {
		panic(err.Error())
	}

	fmt.Println("create table t_articles success")
}
