package model

import (
	"database/sql"
	"fmt"
	"time"
)

type User struct {
	Id 			uint32
	Name 		string
	Created 	time.Time
	Updated 	time.Time
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

func retrieve(id int) (user User, err error) {
	db := ConnectDB()
	defer db.Close()

	user = User{}
	err = db.QueryRow("select id, username, created, updated from t_user where id = ?", id).Scan(
		&user.Id, &user.Name, &user.Created, &user.Updated)
	return
}

func TestUser()  {
	//u1 := &User{
	//	Name: "feng",
	//}
	//err := u1.create()
	//if err != nil {
	//	fmt.Print(err.Error())
	//}

	u2, err := retrieve(1)
	if err != nil {
		fmt.Print(err.Error())
	}
	fmt.Print(u2)

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