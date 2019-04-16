package api

import (
	"backend/model"
	"github.com/gin-gonic/gin"
	"log"
	"net/http"
)

// user register
func Signup(c *gin.Context)  {
	type UserSignupData struct {
		Name 		string 	`json:"name" binding:"required,min=4,max=20"`
		Password 	string 	`json:"password" binding:"required,min=3,max=20"`
	}

	var userInput UserSignupData
	if err := c.ShouldBindJSON(&userInput); err != nil {
		log.Println(err)
		SendErrResp(c, "输入有误，请检查")
		return
	}

	SendResp(c, gin.H{
		"user": userInput,
	})
}

// user login in
func Signin()  {
	
}


func UserList(c *gin.Context)  {
	var users []model.User
	if err := model.DB.Order("id asc").Find(&users).Error; err != nil {
		msg := "can not get user list"
		SendErrResp(c, msg)
		log.Print(msg, err.Error)
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"errNo": ErrCode.SUCCESS,
		"msg": "success",
		"data": gin.H{
			"users": users,
		},
	})
}
