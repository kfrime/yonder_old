package api

import (
	"backend/model"
	"github.com/gin-gonic/gin"
	"log"
	"strconv"
	"strings"
)

func CateList(c *gin.Context)  {
	
}

func CateRetrieve(c *gin.Context)  {
	
}

func saveCate(c *gin.Context) {

}

func CateCreate(c *gin.Context)  {
	type CateData struct {
		Name 		string 	`json:"name" binding:"required,min=3,max=20"`
	}

	var userInput CateData
	if err := c.ShouldBindJSON(&userInput); err != nil {
		log.Println(err)
		SendErrResp(c, "输入有误，请检查")
		return
	}

	var validInput CateData
	if err := Deepcopy(&userInput, &validInput); err != nil {
		SendErrResp(c, "内部错误")
		return
	}

	validInput.Name = preventXSS(userInput.Name)
	validInput.Name = strings.TrimSpace(userInput.Name)
	if validInput.Name != userInput.Name {
		SendErrResp(c, "名称中包含空格")
		return
	}

	var cate model.Category
	err := model.DB.Where("name = ?", validInput.Name).Find(&cate).Error
	if err == nil {
		// 说明该分类已经存在
		if cate.Name == validInput.Name {
			SendErrResp(c, "category {" + cate.Name + "} has been existed.")
			return
		}
	}

	cate.Name = validInput.Name
	if err := model.DB.Create(&cate).Error; err != nil {
		log.Print(err)
		SendErrResp(c, "can not create category")
		return
	}

	SendResp(c, gin.H{
		"cate": cate,
	})

}

func CateUpdate(c *gin.Context)  {
	cateId, err := strconv.Atoi(c.Param("cateId"))
	if err != nil {
		log.Println(err)
		SendErrResp(c, "invalid category id")
		return
	}

	var cate model.Category
	err = model.DB.Where("id = ?", cateId).Find(&cate).Error
	if err != nil {
		log.Println(err)
		SendErrResp(c, "category not existed")
		return
	}

	SendResp(c, gin.H{
		"cate": cate,
	})

}

func CateDestroy(c *gin.Context)  {
	
}
