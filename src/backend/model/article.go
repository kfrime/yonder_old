package model

import (
	"github.com/jinzhu/gorm"
)

type Article struct {
	gorm.Model
	UserId 		uint	`gorm:"not null;index" json:"userId"`
	User 		User
	//CateId 		uint 	`gorm:"not null;index" json:"userId" binding:"required"`
	//Category 	Category
	Title 		string	`gorm:"not null;index" json:"title" binding:"required,min=3,max=20"`
}
