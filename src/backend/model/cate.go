package model

import (
	"errors"
	"log"
	"regexp"

	"github.com/jinzhu/gorm"
)

type Category struct {
	gorm.Model
	Name   string `gorm:"unique;not null;index" json:"name" binding:"required,min=3,max=20"`
}

func (cate *Category) Save() error {
	// 正则判断名称是否正确
	pat := `^[_0-9a-zA-Z]+$`
	if ok, _ := regexp.MatchString(pat, cate.Name); !ok {
		return errors.New("category name is invalid")
	}
	cate.Name = PreventXSS(cate.Name)

	err := DB.Where("name = ?", cate.Name).Find(&cate).Error
	if err == nil {
		//说明该分类已经存在
		return errors.New("category has been existed")
	}

	// create
	if err := DB.Create(&cate).Error; err != nil {
		log.Println(err)
		return errors.New("create category error")
	}

	return nil
}
