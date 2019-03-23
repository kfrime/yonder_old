package config

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"io/ioutil"
)

type dbConfig struct {
	Host 		string
	Port 		int
	User		string
	Password	string
	DbName 		string
	Charset		string
}

type allConfig struct {
	Database 	dbConfig	`json:"database"`
}

// 加载json配置
//var jsonData map[string]interface{}
var AllConfig allConfig

var DB *sql.DB

func loadConf(cfgFile string) {
	data, err := ioutil.ReadFile(cfgFile)
	if err != nil {
		panic(err.Error())
	}

	if err := json.Unmarshal(data, &AllConfig); err != nil {
		panic(err.Error())
	}
	fmt.Println(AllConfig)
}


func initDB() {
	// 数据库相关配置
	var dc dbConfig = AllConfig.Database

	//if err := json.Unmarshal(["database"], &DBConfig); err != nil {
	//	panic(err.Error())
	//}

	mysqlUrl := fmt.Sprintf("%s:%s@%s:%d/%s?charset=%s",
		dc.User, dc.Password, dc.Host, dc.Port, dc.DbName, dc.Charset)
		//DBConfig.User, DBConfig.Password, DBConfig.Host, DBConfig.Port, DBConfig.DbName, DBConfig.Charset)
	fmt.Println(mysqlUrl)
}

func InitJson()  {
	conf := "config.json"
	loadConf(conf)
	initDB()
}
