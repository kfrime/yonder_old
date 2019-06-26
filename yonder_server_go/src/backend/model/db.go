package model

import (
	"fmt"
	"time"

	"github.com/garyburd/redigo/redis"
	"github.com/jinzhu/gorm"

	"backend/config"
)

var DB *gorm.DB

var RedisPool *redis.Pool


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

	// log sql generated by gorm
	db.LogMode(true)

	DB = db
}

func initRedisPool()  {
	var rc = config.AllConfig.Redis
	rdsUrl := fmt.Sprintf("%s:%d", rc.Host, rc.Port)
	RedisPool = &redis.Pool{
		// Maximum number of idle connections in the pool.
		MaxIdle: rc.MaxIdle,

		// max number of connections
		MaxActive: rc.MaxActive,

		IdleTimeout: 3 * 60 * time.Second,

		// Dial is an application supplied function for creating and
		// configuring a connection.
		Dial: func() (redis.Conn, error) {
			c, err := redis.Dial("tcp", rdsUrl)
			if err != nil {
				return nil, err
			}
			return c, err
		},
	}
}

func init()  {
	initDB()
	initRedisPool()
}
