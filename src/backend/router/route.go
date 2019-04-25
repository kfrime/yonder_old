package router

import (
	"backend/api"
	"backend/middleware"
	"github.com/gin-gonic/gin"
)

func Route(router *gin.Engine)  {
	apiGrp := router.Group("/api")
	apiGrp.POST("/user/signup", api.Signup)
	apiGrp.POST("/user/login", api.Login)
	apiGrp.POST("/user/password/update", middleware.LoginRequired,
		api.ResetPasswd)

	apiGrp.POST("/category", api.CateCreate)
}
