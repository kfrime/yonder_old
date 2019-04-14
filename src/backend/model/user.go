package model

import (
	"github.com/jinzhu/gorm"
)

type User struct {
	gorm.Model
	Name 		string		`gorm:"unique;not null;index"`
	Passwd		string		`gorm:"not null" json:"-"`
	Role		int			`gorm:"not null"`
}

// password md5 加密

// user info to redis
