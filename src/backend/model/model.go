package model

import (
	"database/sql"
)

func MigrateModels() {
	var db *sql.DB = ConnectDB()
	if db == nil {
		panic("db is nil")
	}
	defer db.Close()

	tableCreateArticle(db)
	tableCreateUser(db)
	tableCreateCategory(db)
}

