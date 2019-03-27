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

func (user *User) create() (err error) {
	db := ConnectDB()
	defer db.Close()

	stmt, err := db.Prepare("insert into t_user (username) values (?)")
	if err != nil {
		return
	}
	_, err = stmt.Exec(user.Name)
	return err
}

func TestUser()  {
	user := &User{
		Name: "adminuser",
	}
	err := user.create()
	if err != nil {
		fmt.Print(err.Error())
	}
}

func tableCreateUser(db *sql.DB) {
	cmd := `
	create table if not exists t_user (
		id integer not null auto_increment,
		username varchar(100) not null comment 'user name',
		created timestamp not null default current_timestamp,
		updated timestamp not null default current_timestamp on update current_timestamp,
		primary key (id),
		unique key (username)
	) engine=InnoDB default charset=utf8mb4;`

	if _, err := db.Exec(cmd); err != nil {
		panic(err.Error())
	}

	fmt.Println("create table t_user successfully")
}