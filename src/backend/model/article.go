package model

import (
	"errors"
	"github.com/jinzhu/gorm"
	"log"
)

type Article struct {
	gorm.Model
	UserId uint `gorm:"not null;index"`
	//User   User
	CateId 		uint 	`gorm:"not null;index" binding:"required"`
	//Category 	Category
	Title 		string `gorm:"not null;index" binding:"required,min=3,max=20"`
	Content  string 	`binding:"required"`
}

func (ac *Article) checkInput() error {
	ac.Title = PreventXSS(ac.Title)
	ac.Content = PreventXSS(ac.Content)

	// 检查分类是否存在
	if err := IsCateExisted(ac.CateId); err != nil{
		return err
	}

	// 同标题的文章是否存在
	err := DB.Where("title = ?", ac.Title).Find(&ac).Error
	if err == nil {
		//说明该标题已经存在
		return errors.New("article has been existed")
	}
	return nil
}

func (ac *Article) Create() error {
	if err := ac.checkInput(); err != nil {
		return err
	}

	if err := DB.Create(ac).Error; err != nil {
		log.Println(err)
		return errors.New("create article error")
	}

	return nil
}

func (ac *Article) Update(id int) error {
	if err := ac.checkInput(); err != nil {
		return err
	}

	upd := make(map[string]interface{})
	upd["title"] = ac.Title
	upd["cateId"] = ac.CateId
	//upd["userId"] = ac.UserId

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
