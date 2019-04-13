package router

import (
	"github.com/gin-gonic/gin"
)

func userList(c *gin.Context)  {
	c.String(200, "user list")
}

func Route(router *gin.Engine)  {
	api := router.Group("/api")
	api.GET("/user/", userList)
}
