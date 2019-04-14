package model

import (
	"backend/config"
	"backend/debug"
	"crypto/md5"
	"fmt"
	"github.com/jinzhu/gorm"
)

type User struct {
	gorm.Model
	Name 		string		`gorm:"unique;not null;index"`
	Passwd		string		`gorm:"not null" json:"-"`
	Role		int			`gorm:"not null"`
}

func (user User) validPasswd(passswd string) bool {
	if passswd == "" {
		return false
	}
	return true
}

// password md5 加密
func (user User) EncryptPasswd(passwd string) (hashPasswd string) {
	if !user.validPasswd(passwd) {
		dbg.Dbg("password is not valid")
	}

	salt := config.AllConfig.Server.Salt
	p := salt + passwd
	hashPasswd = fmt.Sprintf("%x", md5.Sum([]byte(p)))
	return
}

// user info to redis
