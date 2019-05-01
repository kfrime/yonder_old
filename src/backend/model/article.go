package model

import (
	"errors"
	"github.com/jinzhu/gorm"
	"log"
)

type Article struct {
	gorm.Model
	UserId uint `gorm:"not null;index" json:"userId"`
	User   User
	//CateId 		uint 	`gorm:"not null;index" json:"userId" binding:"required"`
	//Category 	Category
	Title string `gorm:"not null;index" json:"title" binding:"required,min=3,max=20"`
}

func (ac *Article) checkTitle() error {
	ac.Title = PreventXSS(ac.Title)
	return nil
}

func (ac *Article) Create() error {
	if err := ac.checkTitle(); err != nil {
		return err
	}

	if err := DB.Create(ac).Error; err != nil {
		log.Println(err)
		return errors.New("create article error")
	}

	return nil
}

func (ac *Article) Update(id int) error {
	if err := ac.checkTitle(); err != nil {
		return err
	}

	upd := make(map[string]interface{})
	upd["title"] = ac.Title
	upd["userId"] = ac.UserId

	if err := DB.Where("id = ?", id).First(&ac).Error; err != nil {
		log.Println(err)
		return errors.New("article not existed")
	}

	if err := DB.Model(&ac).Updates(upd).Error; err != nil {
		log.Println(err)
		return errors.New("update article error")
	}

	return nil
}
