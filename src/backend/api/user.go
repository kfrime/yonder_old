package api

import (
	"backend/model"
	"github.com/gin-gonic/gin"
	"log"
	"net/http"
)

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
