package config

import (
	"backend/debug"
	"encoding/json"
	_ "github.com/go-sql-driver/mysql"
	"io/ioutil"
)

type DbConfig struct {
	Host 		string
	Port 		int
	User		string
	Password	string
	DbName 		string
	Charset		string
}

type RedisConfig struct {
	Host 		string
	Port 		int
	MaxIdle		int
	MaxActive	int
}

type ServerConfig struct {
	Salt	string
}

type AdminConfig struct {
	Name 		string
	Password 	string
}

type PageConfig struct {
	Size 	uint
}

type allConfig struct {
	Database 	DbConfig		`json:"database"`
	Redis		RedisConfig		`json:"redis"`
	Server 		ServerConfig 	`json:"server"`
	Admin 		AdminConfig 	`json:"admin"`
	Page 		PageConfig		`json:"page"`
}

// 加载json配置
//var jsonData map[string]interface{}
var AllConfig allConfig

func loadConf(cfgFile string) {
	data, err := ioutil.ReadFile(cfgFile)
	if err != nil {
		panic(err.Error())
	}

	if err := json.Unmarshal(data, &AllConfig); err != nil {
		panic(err.Error())
	}
	dbg.Dbg("AllConfig:", AllConfig)
}

func InitConf()  {
	confFile := "config.json"
	loadConf(confFile)
}

func init() {
	InitConf()
}
