package model

import (
	"backend/config"
	"fmt"
	"github.com/jinzhu/gorm"
	"time"
)

var DB *gorm.DB

func initDB()  {
	var dc = config.AllConfig.Database
	mysqlUrl := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=%s&parseTime=true&loc=Local",
		dc.User, dc.Password, dc.Host, dc.Port, dc.DbName, dc.Charset)

	db, err := gorm.Open("mysql", mysqlUrl)
	if err != nil {
		fmt.Println("mysql config: ", mysqlUrl)
		panic(err.Error())
	}
	db.DB().SetConnMaxLifetime(time.Minute * 5)
	db.DB().SetMaxIdleConns(0)
	db.DB().SetMaxOpenConns(10)
	DB = db
}

func init()  {
	initDB()
}
