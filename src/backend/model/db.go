package model

import (
	"backend/config"
	"database/sql"
	"fmt"
)

func ConnectDB() *sql.DB {
	// 数据库相关配置
	var DB *sql.DB

	var dc config.DbConfig = config.AllConfig.Database

	//if err := json.Unmarshal(["database"], &DBConfig); err != nil {
	//	panic(err.Error())
	//}

	mysqlUrl := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=%s&parseTime=true&loc=Local",
		dc.User, dc.Password, dc.Host, dc.Port, dc.DbName, dc.Charset)
	//DBConfig.User, DBConfig.Password, DBConfig.Host, DBConfig.Port, DBConfig.DbName, DBConfig.Charset)

	// 连接数据库
	DB, err := sql.Open("mysql", mysqlUrl)
	if err != nil {
		panic(err.Error())
	}

	//dbg.Dbg("mysqlUrl:", mysqlUrl)
	return DB
}
