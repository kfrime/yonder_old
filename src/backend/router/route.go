package router

import (
	"backend/api"
	"github.com/gin-gonic/gin"
)

func Route(router *gin.Engine)  {
	apiGrp := router.Group("/api")
	apiGrp.GET("/user/", api.UserList)
}
