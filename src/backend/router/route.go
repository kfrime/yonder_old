package router

import (
	"backend/api"
	"backend/middleware"
	"github.com/gin-gonic/gin"
)

func Route(router *gin.Engine)  {
	apiGrp := router.Group("/api")

	// 用户
	apiGrp.POST("/user/signup", api.Signup)
	apiGrp.POST("/user/login", api.Login)
	apiGrp.POST("/user/password/update", middleware.LoginRequired, api.ResetPasswd)

	// 分类
	apiGrp.POST("/category", api.CateCreate)
	apiGrp.PUT("/category/:cateId", api.CateUpdate)
	apiGrp.DELETE("/category/:cateId", api.CateDestroy)
	apiGrp.GET("/category/:cateId", api.CateRetrieve)
	apiGrp.GET("/category", api.CateList)

	// 文章
	apiGrp.POST("/article", middleware.AdminRequired, api.ArticleCreate)
	apiGrp.PUT("/article/:id", middleware.AdminRequired, api.ArticleUpdate)
	apiGrp.DELETE("/article/:id", middleware.AdminRequired, api.ArticleDestroy)
	apiGrp.GET("/article/:id", api.ArticleRetrieve)
	apiGrp.GET("/article", api.ArticleList)
}
