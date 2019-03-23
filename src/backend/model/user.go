package model

import (
	"database/sql"
	"fmt"
	"time"
)

type User struct {
	Id 			uint32
	Name 		string
	created 	time.Duration
	updated 	time.Duration
}

func tableCreateUser(db *sql.DB) {
	cmd := `
	create table if not exists t_user (
		id integer not null auto_increment,
		name varchar(100) not null comment 'user name',
		created timestamp not null default current_timestamp,
		updated timestamp not null default current_timestamp on update current_timestamp,
		primary key (id)
	) engine=InnoDB default charset=utf8mb4;`

	if _, err := db.Exec(cmd); err != nil {
		panic(err.Error())
	}

	fmt.Println("create table t_user successfully")
}