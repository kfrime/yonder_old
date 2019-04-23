package router

import (
	"backend/api"
	"github.com/gin-gonic/gin"
)

func Route(router *gin.Engine)  {
	apiGrp := router.Group("/api")
	apiGrp.POST("/user/signup", api.Signup)
	apiGrp.POST("/user/login", api.Login)
}
