package api

import (
	"backend/model"
	"github.com/gin-gonic/gin"
	"log"
	"strconv"
)

func CateList(c *gin.Context)  {
	// todo: add page and limit
	var cateList []model.Category
	if err := model.DB.Find(&cateList).Error; err != nil {
		log.Println(err)
		SendErrResp(c, err.Error())
		return
	}

	SendResp(c, gin.H{
		"cateList": cateList,
	})
}

func CateRetrieve(c *gin.Context)  {
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

func CateCreate(c *gin.Context)  {
	var cate model.Category
	if err := c.ShouldBindJSON(&cate); err != nil {
		log.Println(err)
		SendErrResp(c, "输入有误，请检查")
		return
	}

	if err := cate.Create(); err != nil {
		SendErrResp(c, err.Error())
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
	if err := c.ShouldBindJSON(&cate); err != nil {
		log.Println(err)
		SendErrResp(c, "输入有误，请检查")
		return
	}

	if err := cate.Update(cateId); err != nil {
		SendErrResp(c, err.Error())
		return
	}

	SendResp(c, gin.H{
		"cate": cate,
	})

}

func CateDestroy(c *gin.Context)  {
	// todo: 该分类下的文章是否还可见？
	cateId, err := strconv.Atoi(c.Param("cateId"))
	if err != nil {
		log.Println(err)
		SendErrResp(c, "invalid category id")
		return
	}

	var cate model.Category
	err = model.DB.First(&cate, "id = ?", cateId).Error
	if err != nil {
		log.Println(err)
		SendErrResp(c, "category not existed")
		return
	}

	if err := model.DB.Delete(&cate).Error; err != nil {
		log.Println(err)
		SendErrResp(c, "delele category error")
		return
	}

	SendResp(c, gin.H{})
}
